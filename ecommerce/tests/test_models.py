from django.test import TestCase
from store.models import Product
from django.db import models

class TestModels(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name ="product_name", price = 20, digital=True, image = '') #Returns name by default 

    def test_product_creation(self):
        self.assertEquals(str(self.product),'product_name') 
        self.assertEquals(self.product.price, 20)
        self.assertEquals(self.product.digital, True)
        self.assertEquals(self.product.image, '')

