from django.test import TestCase
from .models import Item

class TestModel(TestCase):
    def test_default_done_status(self):
        item = Item.objects.create(name='test todo item')
        self.assertFalse(item.done)
