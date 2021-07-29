"""
Aqui no page_helpers é possível criar funções que podem ser reutilizadas
varias vezes dentro dos mapeamentos dos sistemas no page_objects
caso tenha alguma função de validação por exemplo, que serve tanto para um sistema quanto para outro.

"""
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from features.page_objects.Ml.MercadoLivre_index import *


class Page_Helper():

    def __init__(self, context):
        pass
    
    #Por exemplo essa def pode ser utilizada em vários sistemas para a validação, pois não é especifica, é variavel
    def validar_elemento_por_texto(self, context, texto):
        try:
            context.browser.find_element_by_xpath("//*[contains(text(), '{}')]".format(texto))
            return True
        except:
            return "Elemento {} não encontrado".format(texto)