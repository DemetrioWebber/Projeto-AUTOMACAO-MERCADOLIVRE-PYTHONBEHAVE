import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from features.helper.page_helper import *
import time

class MercadoLivre_pesquisa():

    def __init__(self, context):
        self.BTN_DELL                    =  (By.XPATH, '//img[contains(@src, "https://http2.mlstatic.com/D_NP_793290-MLA28058201617_082018-N.webp")]/..')
        self.LISTA_PESQUISA              =  (By.CSS_SELECTOR, '#root-app .ui-search-layout__item')
        self.page_helper                 =  Page_Helper(context)


    def clicar_dell(self, context):
        button_dell = context.browser.find_element(*self.BTN_DELL)
        button_dell.click()
    
    def clicar_primeiro_item(self, context):
        try:
            lista_resultados = context.browser.find_elements(*self.LISTA_PESQUISA)
            lista_resultados[0].click()
        except:
            lista_resultados = context.browser.find_elements(*self.LISTA_PESQUISA)
            lista_resultados[0].click()
    
    def validar_produto_pesquisado(self, context, palavra):
        self.page_helper.validar_elemento_por_texto(context, palavra)

    def validar_lista_produtos(self, context):
        try:
            lista = context.browser.find_elements(*self.LISTA_PESQUISA)
        except:
            assert False, "Produtos não encontrados"
    
    def validar_lista_pesquisada(self, context, lista):
        for item in lista:
            if item != True:
                assert False, item