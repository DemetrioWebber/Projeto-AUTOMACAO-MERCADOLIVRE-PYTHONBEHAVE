import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from features.page_objects.Ml.MercadoLivre_index import *
from features.helper.page_helper import *
from features.fixtures.factory import *
import time


def before_all(context):
    print("-----------------Iniciando teste--------------")
    #instancia do navegador:
    context.browser = webdriver.Chrome()

    #instancia dos Mapeamentos do ML:
    context.mercadolivre = MercadoLivre_index(context)
    #instancia do page_helpers:
    context.page_helper = Page_Helper(context)
    context.browser.implicitly_wait(5)
    #instancia do factory:
    context.factory_json = Json(context)
    

def after_step(context, step):
    pass

def after_all(context):
    print("----------------Encerrando teste---------------")