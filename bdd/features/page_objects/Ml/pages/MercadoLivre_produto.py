import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

class MercadoLivre_produto():

    def __init__(self, context):
        self.BTN_ACEITAR_COOKIE          =  (By.ID, 'cookieDisclaimerButton')
        self.BTN_ADD_CARRINHO            =  (By.XPATH, '//button[contains(@formaction, "https://www.mercadolivre.com.br/gz/cart/item/add")]')

    def adicionar_carrinho(self, context):
        botao_aceitar_cookie = context.browser.find_element(*self.BTN_ACEITAR_COOKIE)
        botao_carrinho = context.browser.find_element(*self.BTN_ADD_CARRINHO)
        botao_aceitar_cookie.click()
        botao_carrinho.click()
    
    def validar_tentativa_adicionar_carrinho(self, context):
        try:
            context.browser.find_element_by_xpath("//*[contains(text(), 'Olá! Para adicionar ao carrinho, acesse a sua conta')]")
        except:
            assert False, "Erro ao adicionar produto ao carrinho"