# Prova Desenvolvedor

Resolução da prova para desenvolvedor. A linguagem escolhida para a resolução é Python.

Optei por utilizar uma abordagem orientada a objetos, utilizando polimorfismo
para resolver os diferentes métodos de obter o valor do orçamento por tipo de petshop.
Para os algoritmos de cálculo e escolha do orçamento, adotei uma abordagem mais procedural,
aproveitando a flexibilidade da linguagem para manter a simplicidade e legibilidade do código.

Implementei testes unitários para validar todas as regras estabelecidas.

### Organização do projeto:

- [app.py](app.py): Ponto de entrada. Definição da interface de linha de comando.
- [petshop.py](petshop.py): Definição dos diferentes tipos de petshop, representados por classes.
- [canil.py](canil.py): Regras de negócio. Contém a função que determina o melhor orçamento.
- [test.py](test.py): Testes unitários.

### Executando a aplicação:

```
python app.py <data> <quantidade de cães pequenos> <quantidade de cães grandes>
```

Exemplo:
```sh
python app.py 03/08/2018 3 5
```

### Executando testes:

```sh
python tests.py
```
