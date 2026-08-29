from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            Title='Pizza', 
            Price=10.99, 
            Inventory=5
        )
        
        self.assertEqual(str(item), 'Pizza : 10.99')