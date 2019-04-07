from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from menu.models import Menu, Item, Ingredient


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.menu = Menu.objects.create(
            season='TestSeason',
            created_date=datetime.now(),
            expiration_date=datetime.now(),
        )
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
        self.ingredient = Ingredient.objects.create(
            name='TestIngredient'
        )

    def test_menu_list(self):
        response = self.client.get(reverse('menu:menu_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/list_all_current_menus.html')

    def test_menu_detail(self):
        response = self.client.get(reverse('menu:menu_detail',
                                           kwargs={'pk': self.menu.pk}
                                           ))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu_detail.html')

    def test_item_detail(self):
        response = self.client.get(reverse('menu:item_detail',
                                           kwargs={'pk': self.item.pk}
                                           ))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/detail_item.html')

    def test_item_detail_404(self):
        response = self.client.get(reverse('menu:item_detail',
                                           kwargs={'pk': '999999999'}
                                           ))
        self.assertEquals(response.status_code, 404)

    def test_create_new_menu(self):
        response = self.client.get(reverse('menu:menu_new'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu_edit.html')

    def test_edit_menu(self):
        response = self.client.get(reverse('menu:menu_edit',
                                           kwargs={'pk': self.menu.pk}
                                           ))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu_edit.html')
