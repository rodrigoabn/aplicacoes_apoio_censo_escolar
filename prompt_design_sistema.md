AJA COMO UM ESPECIALISTA EM FRONT-END E DESIGN SYSTEM.

Refatore o estilo do projeto atual aplicando estritamente a identidade visual descrita abaixo.

⚠️ DIRETRIZ CRÍTICA: Não crie novos componentes, novas linhas de HTML, novas lógicas ou novas mensagens. Altere APENAS o CSS/estilização dos elementos já existentes na aplicação.

### 1. Paleta de Cores (Tokens de Design)
Aplique estas variáveis no `:root` do CSS para centralizar as cores:
* **Fundos:** Geral: `#131722` | Cards/Painéis: `#1e222d` | Sidebar: `#171b26`.
* **Bordas:** Padrão: `#2a2e39` | Linhas sutis: `rgba(255,255,255,0.07)`.
* **Texto:** Principal: `#ffffff` | Secundário: `#b2b5be` | Muted/Placeholders: `rgba(232,229,222,0.35)`.
* **Status (20% opacidade no fundo):** * OK (Verde): `#22c55e` / `rgba(34, 197, 94, 0.2)`
    * Atenção (Amarelo): `#eab308` / `rgba(234, 179, 8, 0.2)`
    * Crítico (Vermelho): `#ef4444` / `rgba(239, 68, 68, 0.2)`
    * Info (Azul): `#3b82f6` / `rgba(59, 130, 246, 0.2)`
* **Arredondamento:** `sm: 6px` | `md: 8px` | `lg: 12px`.

### 2. Tipografia e Elementos Globais
* **Fonte:** `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif`.
* **Hierarquia:** `h1` (1.95rem, bold 600, branco), `h2` (1.05rem, 600), `h3` (0.9rem, 600).
* **Rótulos/Labels:** Caixa alta (`uppercase`), tamanho `0.7rem`, peso `600`, cor secundária.
* **Focus:** Outline azul `3px solid #3b82f6` com `outline-offset: 2px`.

### 3. Layout, Sidebar e Menu de Navegação
* **Container Principal:** Centralizado, largura máxima `1400px`, padding lateral `1.5rem`.
* **Sidebar:** Largura fixa `280px`, fundo `#171b26`, borda direita padrão.
* **Menu (Itens Horizontais/Verticais):**
    * *Inativo:* Fundo transparente, sem bordas (exceto esquerda `3px solid transparent`), cor secundária, peso `500`, tamanho `0.80rem`.
    * *Hover:* Fundo `rgba(255,255,255,0.08)`, texto principal.
    * *Ativo:* Fundo `rgba(59,130,246,0.08)`, borda esquerda azul (`#3b82f6`), texto `#f0f0f0`.

### 4. Cards (KPIs e Secundários), Painéis e Tooltips
* **Estilo Base:** Fundo `#1e222d`, borda padrão, cantos `8px`. Hover muda borda para `rgba(255,255,255,0.12)`.
* **KPIs (Valores):** Título pequeno/uppercase. Valor grande (`1.65rem`, negrito `700`). Deltas inferiores usam cores críticas (vermelho para alta ruim, verde para baixa boa) e ícones (`↑`, `↓`, `→`).
* **Painéis (Panels):** Cabeçalho com padding `14px 18px 12px` e linha divisória. Corpo com padding `16px 18px`.
* **Tooltips (ⓘ):** Círculo de `16px`, cursor `help`. Balão flutuante acima com fundo `#1e222d` e sombra.

### 5. Botões, Controles e Pills (Filtros)
* **Botão Padrão:** Transparente, texto branco, borda `1px solid #454955`, raio `6px`. Hover ativa fundo `rgba(255,255,255,0.05)`.
* **Botão Sucesso:** Borda e texto verdes.
* **Pills/Tags de Filtro:** Arredondados (`12px`), compactos, texto muted. *Ativo:* Borda azul, fundo azul translúcido (`rgba(59, 130, 246, 0.12)`), texto azul claro.
* **Dropdowns:** Altura compacta (`26px`/`28px`).

### 6. Tabelas e Badges de Status
* **Tabela Mapa de Calor:** Células espaçadas (`3px` a `5px`), cantos `4px`, negrito `600`. Cores de fundo e texto variam conforme o status (Crítico = fundo vermelho a 20%, texto claro; Atenção = amarelo; OK = verde).
* **Tabela de Listagem:** Borda externa com cantos `8px`. Cabeçalho com fundo sutil. Linhas com hover suave. Células com texto truncado (`ellipsis`) se passarem de `250px`.
* **Badges:** Estilo `inline-flex`, compactos (`padding: 3px 7px`), cantos `4px`, peso `600`, aplicando as cores e fundos respectivos do status.
* **Banners de Alerta:** Fundo amarelo sutil (`rgba(234,179,8,0.07)`), borda amarela, texto escurecido (`#a16207`).