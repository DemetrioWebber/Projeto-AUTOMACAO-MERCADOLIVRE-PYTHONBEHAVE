import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from features.page_objects.Ml.MercadoLivre_index import *
from features.helper.page_helper import *
import time


def before_all(context):
    print("-----------------Iniciando teste--------------")
    #instancia do navegador:
    context.chrome_options = Options()
    context.chrome_options.add_argument('--headless')
    context.browser = webdriver.Chrome(chrome_options=context.chrome_options)
    # context.browser = webdriver.Chrome()

    #instancia dos Mapeamentos do ML:
    context.mercadolivre = MercadoLivre_index(context)
    #instancia do page_helpers:
    context.page_helper = Page_Helper(context)
    context.browser.implicitly_wait(5)

def after_step(context, step):
    pass

def after_all(context):
    print("----------------Encerrando teste---------------")