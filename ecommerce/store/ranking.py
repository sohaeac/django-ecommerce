from .models import *
import random

class Ranking:
    def addBoughtProducts(self):
        pass
    def topOrderedProducts(self):
        products = Product.objects.all()
        topProducts = []
        for i in products:
                topProducts.append(i)
        return random.sample(topProducts,5)
