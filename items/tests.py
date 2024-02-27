from django.test import TestCase
from .models import Items
# Create your tests here.

class ItemsTest(TestCase):
  """Test module for Items Model"""
  def setUp(self):
    Items.objects.create(name ="UG", price="32000.00", description="The spirit that binds us")
    Items.objects.create(name ="jameson", price="240000.00", description="Irish Whiskey")
  
  def test_get_items(self):
    get_items = Items.objects.get(name="UG")
    # print(">>>>>", get_items.name)
    self.assertEqual(get_items.name, "UG" )
