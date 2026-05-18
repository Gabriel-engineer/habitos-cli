# Como Contribuir

Obrigado pelo interesse em contribuir com o **Hábitos CLI**!

## Fluxo de trabalho

1. Faça um fork do repositório
2. Crie uma branch para sua feature: `git checkout -b feature/minha-feature`
3. Implemente suas alterações
4. Garanta que os testes passam: `pytest`
5. Garanta que o lint passa: `ruff check src/ tests/`
6. Faça commit seguindo o padrão: `git commit -m "feat: descrição da mudança"`
7. Envie para seu fork: `git push origin feature/minha-feature`
8. Abra um Pull Request para a branch `main`

## Padrão de commits

- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` atualização de documentação
- `test:` adição ou correção de testes
- `refactor:` refatoração sem mudança de comportamento
- `chore:` tarefas de manutenção

## Ambiente de desenvolvimento

```bash
git clone https://github.com/seu-usuario/habitos-cli.git
cd habitos-cli
pip install -e ".[dev]"
```
