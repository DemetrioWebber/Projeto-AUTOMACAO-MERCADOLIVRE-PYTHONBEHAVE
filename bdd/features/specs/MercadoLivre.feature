#language: pt

@feature.adicionar_ao_carrinho
Funcionalidade: Carrinho e Busca no MercadoLivre

    @scenario.notebook_dell
    Cenário: Pesquisar por Notebook Dell

        Dado que esteja na pagina home
        E que a barra de pesquisa esteja visível
        Quando pesquisar por um produto "Notebook"
        E escolher a marca Dell
        E escolher o primeiro produto
        Então deverá ser exibido a página do produto

    @scenario.produto_exemplo
    Esquema do Cenário: Buscar um produto dinâmico

        Dado que esteja na pagina home
        E que a barra de pesquisa esteja visível
        Quando pesquisar por um produto "<produto>"
        E aguardar os resultados
        Então deverá ser validado a busca por "<produto>"
        Exemplos:
            | produto    |
            | Cafeteira  |
            | Tv smart   |
            | Smartphone |

    @scenario.produto_fixture
    Cenário: Buscar um produto dinâmico por json

        Dado que esteja na pagina home
        E que possua um json com diversos produtos
        Quando pesquisar pelos produtos no MercadoLivre
        Então a busca pelos produtos é validada