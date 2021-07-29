from behave import given, when, then
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time

# ----------------- Steps Comuns aos cenários ------------------
@given(u'que esteja na pagina home')
def acessar_home(context):
    context.mercadolivre.home.acessar_ML(context)

@given(u'que a barra de pesquisa esteja visível')
def valida_barra_pesquisa(context):
    context.mercadolivre.home.validar_barra_de_busca(context)

@when(u'pesquisar por um produto "{produto}"')
def pesquisar_produto(context, produto):
    context.mercadolivre.home.procurar_produto(context, produto)

# ----------------- Steps @scenario.notebook_dell ------------------

@when(u'escolher a marca Dell')
def selecionar_marca_dell(context):
    context.mercadolivre.pesquisa.clicar_dell(context)


@when(u'escolher o primeiro produto')
def escolhe_primeiro_produto(context):
    context.mercadolivre.pesquisa.clicar_primeiro_item(context)


@then(u'deverá ser exibido a página do produto')
def adicionar_ao_carinho(context):
    context.mercadolivre.produto.validar_tela_do_produto(context)
    


# ------------------- Steps exclusivos @scenario.produto_exemplo -----------------------

@when(u'aguardar os resultados')
def step_impl(context):
    context.mercadolivre.pesquisa.validar_lista_produtos(context)


@then(u'deverá ser validado a busca por "{produto}"')
def step_impl(context, produto):
    context.mercadolivre.pesquisa.validar_produto_pesquisado(context, produto)



# ------------------- Steps exclusivos @scenario.produto_fixture -----------------------

@given(u'que possua um json com diversos produtos')
def step_impl(context):
    context.json_produtos = context.factory_json.retornarJson("produtos.json")


@when(u'pesquisar pelos produtos no MercadoLivre')
def step_impl(context):
    context.mercadolivre.home.procurar_produtos_arquivo(context, context.json_produtos["Busca"]["Produtos"])


@then(u'a busca pelos produtos é validada')
def step_impl(context):
    context.mercadolivre.pesquisa.validar_lista_pesquisada(context, context.items_validados)