from .models import *
import random
import redis
from django.conf import settings
import operator

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=4)

class Ranking:
    sorted_liste = []
    def addBoughtProducts(self,bought_products):
        self.bought_products = bought_products
        products_bought = {}
        for i in bought_products:
            r.incr("prod:{}".format(i.product))
            products_bought[i] = int(r.get("prod:{}".format(i.product)))
        
        dico_ord = dict(sorted(products_bought.items(), key=operator.itemgetter(1)))
        self.sorted_liste.append(dico_ord)
        
    
    def topOrderedProducts(self):
        '''products = Product.objects.all()
        topProducts = []
        for i in products:
                topProducts.append(i)
        return random.sample(topProducts,5)
        '''
        #print('Je suis iciiiii')
        #print(self.sorted_liste)

        products = Product.objects.all()
        if len(self.sorted_liste) == 0:
            return(random.sample(list(products),5))
        else: 
            topProducts = []
            test = self.sorted_liste[0].keys()
            print(test)
            for i in test:
                topProducts.append(i.product)
            return(topProducts)
    
    def clear_sorted_liste(self):
        self.sorted_liste = []

        

    
