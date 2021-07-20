#language: pt

@feature.adicionar_ao_carrinho
Funcionalidade: Carrinho e Busca no MercadoLivre

    @scenario.notebook_dell
    Cenário: Adicionar Notebook Dell ao carrinho

        Dado que acesse a pagina home
        E que a barra de pesquisa esteja visível
        Quando pesquisar por um Notebook da marca Dell
        E escolher o primeiro Notebook
        Então deve mostrar a página do produto

    @scenario.produto_exemplo
    Esquema do Cenário: Buscar um produto dinâmico

        Dado que acesse a pagina home
        E que a barra de pesquisa esteja visível
        Quando pesquisar por um "<produto>"
        E trazer os resultados
        Então deve validar a busca por "<produto>"

        Exemplos:
            | produto    |
            | Cafeteira  |
            | Tv smart   |
            | Smartphone |
