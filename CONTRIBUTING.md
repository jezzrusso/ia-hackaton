# Contribuindo

Obrigado por contribuir com este projeto.

## Fluxo recomendado

1. Crie uma branch descritiva.
2. Faça mudanças pequenas e com escopo claro.
3. Execute verificações locais (`make check`).
4. Abra PR com descrição objetiva do problema e da solução.

## Padrões de código

- Python com tipagem gradual e nomes autoexplicativos.
- Evite mudanças de comportamento sem necessidade.
- Prefira funções pequenas e com responsabilidade única.
- Mantenha comentários para contexto de negócio, não para descrever o óbvio.

## Commits

Use mensagens claras no imperativo, por exemplo:

- `docs: melhora guia de execução no README`
- `chore: adiciona configuração de lint no pyproject`

## Checklist antes do PR

- [ ] Projeto continua executando sem regressões funcionais.
- [ ] Comandos de validação passaram localmente.
- [ ] Documentação atualizada quando aplicável.
