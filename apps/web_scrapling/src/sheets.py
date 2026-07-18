"""Escrita incremental na Planilha Google (destino dos dados coletados).

A única escrita permitida pela cláusula pétrea é nesta planilha do usuário.
O site Educacenso NUNCA recebe escrita (ver scraper.py / auth.py).
"""

from __future__ import annotations

import re

import gspread
from google.oauth2.service_account import Credentials

import src.modelo as modelo
from src.modelo import DOCS_DIR, KEY_COLUMNS, load_model

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

CREDENTIALS_PATH = DOCS_DIR / "credenciais.json"
KEY_COL_INDEX = 0  # coluna "Código do Inep" (primeira coluna do modelo)


def _extract_id(link: str) -> str:
    """Extrai o ID da planilha a partir de um link de compartilhamento."""
    m = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", link)
    if m:
        return m.group(1)
    # Talvez o usuário tenha colado só o ID.
    if re.fullmatch(r"[a-zA-Z0-9-_]{20,}", link.strip()):
        return link.strip()
    raise ValueError("Link da planilha inválido ou ID não reconhecido.")


def get_client() -> gspread.Client:
    creds = Credentials.from_service_account_file(str(CREDENTIALS_PATH), scopes=SCOPES)
    return gspread.authorize(creds)


def open_sheet(client: gspread.Client, link: str) -> gspread.Spreadsheet:
    return client.open_by_key(_extract_id(link))


# Abas que o sistema NUNCA deve criar, escrever ou manter na planilha.
# A aba "Seleção" não faz parte do modelo de extração e deve ser removida
# caso já exista na planilha do usuário.
FORBIDDEN_SHEETS = {"Seleção", "Selecao", "Selection"}


def ensure_structure(spreadsheet: gspread.Spreadsheet) -> None:
    """Garante que as 6 abas existam com o cabeçalho do modelo.

    Se a aba não existir, é criada. Se existir e estiver vazia, o cabeçalho
    é escrito. Não sobrescreve dados existentes. Abas proibidas (ex.:
    "Seleção") são ignoradas e removidas se presentes.
    """
    model = load_model()
    existing = {ws.title for ws in spreadsheet.worksheets()}
    # Remove abas proibidas que porventura já existam na planilha.
    for title in list(existing):
        if title in FORBIDDEN_SHEETS:
            spreadsheet.del_worksheet(spreadsheet.worksheet(title))
            existing.discard(title)
    for sheet, cols in model.items():
        title = SHEET_NAME_ALIASES.get(sheet, sheet)
        if title in FORBIDDEN_SHEETS:
            continue
        if title not in existing:
            ws = spreadsheet.add_worksheet(title=title, rows=1000, cols=max(len(cols), 2))
        else:
            ws = spreadsheet.worksheet(title)
        # Escreve cabeçalho apenas se a primeira linha estiver vazia.
        first = ws.row_values(1)
        if not any(str(c).strip() for c in first):
            ws.update(values=[cols], range_name="A1")


# Mapeia o nome da aba no modelo para o nome real na planilha do usuário.
SHEET_NAME_ALIASES = {
    "Vinculação institucional e Conv": "Vinculação",
    "Funcionamento e Identificação": "Funcionamento",
    "Estrutura física": "Estrutura",
    "Equipamentos e recursos tecnoló": "Equipamentos",
    "Recursos humanos": "RH",
    "Organização escolar": "Organização",
}


def _find_row_by_inep(ws: gspread.Worksheet, codigo: str) -> int | None:
    """Retorna o número da linha (1-based) onde o Código do Inep aparece."""
    try:
        col = ws.col_values(KEY_COL_INDEX + 1)
    except Exception:
        return None
    for idx, val in enumerate(col[1:], start=2):  # pula cabeçalho
        if str(val).strip() == str(codigo).strip():
            return idx
    return None


def write_school(spreadsheet: gspread.Spreadsheet, dados: dict[str, dict]) -> None:
    """Grava os dados de UMA escola de forma incremental em cada aba.

    Atualiza a linha existente (pelo Código do Inep) ou insere nova linha.
    Reabre o worksheet a cada escola para não manter cache pesado.
    """
    model = load_model()
    for sheet, row in dados.items():
        cols = model[sheet]
        title = SHEET_NAME_ALIASES.get(sheet, sheet)
        ws = spreadsheet.worksheet(title)
        values = [row.get(c, "") for c in cols]

        linha = _find_row_by_inep(ws, row.get("Código do Inep", ""))
        if linha is None:
            ws.append_row(values)
        else:
            # Atualiza célula a célula (evita sobrescrever colunas alheias).
            for col_idx, val in enumerate(values, start=1):
                ws.update_cell(linha, col_idx, val)
