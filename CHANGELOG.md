# Changelog

Todas as mudanças relevantes deste projeto serão documentadas aqui.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adota [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [1.0.0] - 2025-01-01

### Adicionado
- Interface CLI com os comandos: `adicionar`, `listar`, `concluir`, `remover` e `resumo`
- Persistência local dos hábitos em arquivo JSON (`~/.habitos_cli/data.json`)
- Separação por data: cada dia tem seu próprio registro de hábitos
- Barra de progresso visual no comando `resumo`
- Testes automatizados com `pytest` cobrindo os principais fluxos
- Linting e verificação de formatação com `ruff`
- Pipeline de CI com GitHub Actions (lint + testes automáticos)
- Documentação completa no `README.md`
- Arquivo `LICENSE` (MIT)
