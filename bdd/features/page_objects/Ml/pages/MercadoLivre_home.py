import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from features.helper.page_helper import *

class MercadoLivre_home():
    
    def __init__(self, context):
        self.INPUT_PROCURAR              =  (By.NAME, "as_word")
        self.BTN_BUSCAR                  =  (By.CLASS_NAME, "nav-search-btn")
        self.page_helper                 =  Page_Helper(context)

    def acessar_ML(self, context):
        context.browser.get("https://www.mercadolivre.com.br/")


    def validar_barra_de_busca(self, context):
        input_procurar = context.browser.find_element(*self.INPUT_PROCURAR)
        if input_procurar.is_displayed():
            print("Barra de busca validada")
        else:
            assert False, "Impossível validar a barra de busca"


    def procurar_produto(self, context, produto):
        input_procurar = context.browser.find_element(*self.INPUT_PROCURAR)
        buscar = context.browser.find_element(*self.BTN_BUSCAR)

        input_procurar.send_keys(produto)
        buscar.click()
    
    def procurar_produtos_arquivo(self, context, produtos):
        context.items_validados = list()
        for item in produtos:
            self.procurar_produto(context, item)
            validado = self.page_helper.validar_elemento_por_texto(context, item)
            context.items_validados.append(validado)
            self.acessar_ML(context)
