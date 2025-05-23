from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Dessert")
        self.assertEqual(str(category), "Dessert")
        self.assertEqual(list(iter(category)), list("Dessert"))

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main Course")
    
    def test_create_recipe(self):
        recipe = Recipe.objects.create(
            title="Borscht",
            description="Traditional Ukrainian beet soup",
            instructions="1. Chop vegetables\n2. Boil water\n3. Add ingredients",
            ingredients="Beetroot, Potatoes, Carrots, Onion, Cabbage",
            category=self.category
        )
        self.assertEqual(str(recipe), "Borscht")
        self.assertEqual(recipe.category.name, "Main Course")
        self.assertIsNotNone(recipe.created_at)
        self.assertIsNotNone(recipe.updated_at)