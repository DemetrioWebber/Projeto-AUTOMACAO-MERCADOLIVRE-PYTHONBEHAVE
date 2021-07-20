from behave import given, when, then
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time

# ----------------- Steps @scenario.notebook_dell ------------------
@given(u'que esteja a pagina home')
def acessar_home(context):
    context.mercadolivre.home.acessar_ML(context)


@given(u'que a barra de pesquisa esteja visível')
def valida_barra_pesquisa(context):
    context.mercadolivre.home.validar_barra_de_busca(context)


@when(u'pesquisar por um Notebook da marca Dell')
def pesquisar_notebook_dell(context):
    context.mercadolivre.home.procurar_produto(context, "Notebook")
    context.mercadolivre.pesquisa.clicar_dell(context)


@when(u'escolher o primeiro Notebook')
def escolhe_primeiro_Notebook(context):
    context.mercadolivre.pesquisa.clicar_primeiro_item(context)
    context.mercadolivre.produto.adicionar_carrinho(context)


@then(u'deve mostrar a página do produto')
def adicionar_ao_carinho(context):
    context.mercadolivre.produto.validar_tentativa_adicionar_carrinho(context)
    

# ------------------- Steps exclusivos @scenario.produto_exemplo -----------------------

@when(u'pesquisar por um "{produto}"')
def pesquisar_produto(context, produto):
    context.mercadolivre.home.procurar_produto(context, produto)


@when(u'trazer os resultados')
def step_impl(context):
    context.mercadolivre.pesquisa.validar_lista_produtos(context)


@then(u'deve validar a busca por "{produto}"')
def step_impl(context, produto):
    context.mercadolivre.pesquisa.validar_produto_pesquisado(context, produto)