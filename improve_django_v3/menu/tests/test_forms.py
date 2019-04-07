from django.utils import timezone
from django.contrib.auth.models import User
from django.test import TestCase

from menu.forms import MenuForm
from menu.models import Menu, Item


class TestForms(TestCase):

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
            created_date=timezone.now(),
        )

        self.item2 = Item.objects.create(
            name='TestName2',
            description='TestDescription2',
            chef=self.user,
            created_date=timezone.now(),
        )

        self.menu = Menu.objects.create(
            season='TestSeason',
            created_date=timezone.now(),
            expiration_date=timezone.now(),
        )
        self.menu.items.add(self.item, self.item2)

    def test_menu_form_valid_data(self):

        form = MenuForm(data={
            'season': self.menu.season,
            'items': ['1', '2'],
            'expiration_date': self.menu.expiration_date
        })

        self.assertTrue(form.is_valid())

    def test_menu_form_no_data(self):
        form = MenuForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_menu_form_invalid_season(self):

        form = MenuForm(data={
            'season': 'sea',
            'items': ['1', '2'],
            'expiration_date': self.menu.expiration_date
        })

        self.assertFalse(form.is_valid())

    def test_menu_form_invalid_items(self):

        form = MenuForm(data={
            'season': self.menu.season,
            'items': ['1'],
            'expiration_date': self.menu.expiration_date
        })

        self.assertFalse(form.is_valid())
