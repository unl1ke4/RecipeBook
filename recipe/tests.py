from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Dessert")
        self.assertEqual(str(category), "Dessert")
        self.assertEqual(list(iter(category)), list("Dessert"))