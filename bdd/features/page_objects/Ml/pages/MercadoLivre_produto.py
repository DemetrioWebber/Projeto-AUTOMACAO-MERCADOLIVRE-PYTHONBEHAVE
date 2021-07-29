import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time

class MercadoLivre_produto():

    def __init__(self, context):
        self.BTN_ACEITAR_COOKIE          =  (By.ID, 'newCookieDisclaimerButton')
        self.BTN_ADD_CARRINHO            =  (By.XPATH, '//button[contains(@formaction, "https://www.mercadolivre.com.br/gz/cart/item/add")]')

    def adicionar_carrinho(self, context):
        botao_aceitar_cookie = context.browser.find_element(*self.BTN_ACEITAR_COOKIE)
        botao_carrinho = context.browser.find_element(*self.BTN_ADD_CARRINHO)
        botao_aceitar_cookie.click()
        botao_carrinho.click()
    
    def validar_tela_do_produto(self, context):
        try:
            context.browser.find_element_by_xpath("//*[contains(text(), 'Voltar à lista')]")
        except:
            assert False, "Erro ao acessar página do produto!"

    