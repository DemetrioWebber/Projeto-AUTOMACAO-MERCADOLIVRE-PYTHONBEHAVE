from features.page_objects.Ml.pages.MercadoLivre_home import *
from features.page_objects.Ml.pages.MercadoLivre_pesquisa import *
from features.page_objects.Ml.pages.MercadoLivre_produto import *

class MercadoLivre_index():

    def __init__(self, context):
        self.home = MercadoLivre_home(context)
        self.pesquisa = MercadoLivre_pesquisa(context)
        self.produto = MercadoLivre_produto(context)
        context.browser.implicitly_wait(5)


