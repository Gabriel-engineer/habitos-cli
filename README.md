# ✅ Hábitos CLI

[![CI](https://github.com/seu-usuario/habitos-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/seu-usuario/habitos-cli/actions/workflows/ci.yml)
![Versão](https://img.shields.io/badge/versão-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Licença](https://img.shields.io/badge/licença-MIT-green)

> Checklist de hábitos diários pelo terminal — simples, leve e sem distrações.

---

## 🎯 Problema Real

Manter hábitos saudáveis é um desafio comum. Segundo estudos de psicologia comportamental, a falta de registro e acompanhamento é uma das principais causas de abandono de rotinas como beber água, praticar exercícios ou meditar. Muitas pessoas desejam uma ferramenta simples, que não exija cadastro em aplicativos, sem distrações e que funcione diretamente no terminal.

## 💡 Proposta de Solução

O **Hábitos CLI** é uma ferramenta de linha de comando (CLI) que permite ao usuário cadastrar hábitos diários, marcá-los como concluídos e acompanhar seu progresso — tudo pelo terminal, sem dependências externas e com dados salvos localmente.

## 👥 Público-Alvo

- Pessoas que querem acompanhar hábitos de forma simples
- Desenvolvedores e usuários que preferem ferramentas de terminal
- Qualquer pessoa que deseje reduzir o uso de aplicativos pesados para tarefas simples

---

## ✨ Funcionalidades

| Comando | Descrição |
|---|---|
| `habitos adicionar <nome>` | Adiciona um hábito para o dia de hoje |
| `habitos listar` | Lista todos os hábitos do dia com status |
| `habitos concluir <nome>` | Marca um hábito como concluído |
| `habitos remover <nome>` | Remove um hábito do dia |
| `habitos resumo` | Exibe barra de progresso e estatísticas do dia |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** — linguagem principal
- **argparse** — interface de linha de comando (biblioteca padrão)
- **json** — persistência local de dados (biblioteca padrão)
- **pytest** — testes automatizados
- **ruff** — linting e verificação de formatação
- **GitHub Actions** — integração contínua (CI)

---

## 📦 Instalação

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/habitos-cli.git
cd habitos-cli

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

# 3. Instale o projeto
pip install -e .
```

---

## ▶️ Execução

```bash
# Adicionar hábitos
habitos adicionar "Beber 2L de água"
habitos adicionar "Meditar 10 minutos"
habitos adicionar "Caminhar 30 minutos"

# Listar hábitos do dia
habitos listar

# Marcar como concluído
habitos concluir "Meditar 10 minutos"

# Ver progresso
habitos resumo

# Remover um hábito
habitos remover "Caminhar 30 minutos"
```

### Exemplo de saída

```
$ habitos listar

📋 Hábitos de hoje (3 total):

  [✓] Meditar 10 minutos
  [○] Beber 2L de água
  [○] Caminhar 30 minutos

$ habitos resumo

📊 Progresso do dia: [█░░░░░░░░░] 33%
   ✓ Concluídos : 1
   ○ Pendentes  : 2
   Total        : 3
```

---

## 🧪 Rodando os Testes

```bash
# Instalar dependências de desenvolvimento
pip install -e ".[dev]"

# Executar todos os testes
pytest

# Com detalhes
pytest -v
```

---

## 🔍 Rodando o Lint

```bash
# Verificar problemas de estilo e qualidade
ruff check src/ tests/

# Verificar formatação
ruff format --check src/ tests/
```

---

## 📁 Estrutura do Projeto

```
habitos-cli/
├── src/
│   └── habitos/
│       ├── __init__.py      # versão do pacote
│       ├── main.py          # interface CLI (entry point)
│       ├── manager.py       # lógica de negócio
│       └── storage.py       # persistência em JSON
├── tests/
│   ├── conftest.py
│   ├── test_manager.py      # testes da lógica principal
│   └── test_storage.py      # testes do módulo de armazenamento
├── .github/
│   └── workflows/
│       └── ci.yml           # pipeline de CI
├── pyproject.toml           # configuração do projeto, dependências, ruff, pytest
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

---

## 📌 Versão Atual

**1.0.0** — Veja o [CHANGELOG](CHANGELOG.md) para o histórico de mudanças.

---

## 👤 Autor

**Seu Nome**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)

---

## 🔗 Repositório

[https://github.com/seu-usuario/habitos-cli](https://github.com/seu-usuario/habitos-cli)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
