from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class MenuViewTest(TestCase):

    def setUp(self):
        
          
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        Menu.objects.create(
            Title='Pizza',
            Price=10.99,
            Inventory=5
        )

        Menu.objects.create(
            Title='Burger',
            Price=8.99,
            Inventory=10
        )

    def test_getall(self):
        
        client = APIClient()
        
        
        client.force_authenticate(user=self.user)

    
        response = client.get('/api/menu/')

        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)

        self.assertEqual(response.data, serializer.data)