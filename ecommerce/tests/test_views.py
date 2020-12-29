from django.test import TestCase, Client 
from django.urls import reverse
from store.models import Customer, Product, Order, OrderItem, ShippingAddress
import json

class TestViews(TestCase):

    def setUp(self): #Runs before every single test method 
        self.client = Client()
        self.store_url = reverse('store')
        self.cart_url = reverse('cart')


    def test_store_GET(self):

        response = self.client.get(self.store_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')
    
    def test_cart_GET(self):
        response = self.client.get(self.cart_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')

