from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from menu.models import Menu, Item, Ingredient


class TestMenuModel(TestCase):

    def setUp(self):
        self.menu = Menu.objects.create(
            season='TestSeason',
            created_date=datetime.now(),
            expiration_date=datetime.now(),
        )

    def test_menu_creation(self):
        menu = self.menu
        self.assertTrue(isinstance(menu, Menu))


class TestItemModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name='TestUser',
            last_name='TestLastName',
            email='test@email.com',
            password='SuperSecret',
        )
        self.item = Item.objects.create(
            name='TestName',
            description='TestDescription',
            chef=self.user,
            created_date=datetime.now(),
        )

    def test_item_creation(self):
        item = self.item
        self.assertTrue(isinstance(item, Item))


class TestIngredientModel(TestCase):

    def setUp(self):
        self.ingredient = Ingredient.objects.create(
            name='TestIngredient'
        )

    def test_ingredient_creation(self):
        ingredient = self.ingredient
        self.assertTrue(isinstance(ingredient, Ingredient))
