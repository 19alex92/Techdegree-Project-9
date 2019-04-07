from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import (menu_list, menu_detail, item_detail,
                        create_new_menu, edit_menu)


class TestUrls(SimpleTestCase):

    def test_menu_list_url_is_resolved(self):
        url = reverse('menu:menu_list')
        self.assertEquals(resolve(url).func, menu_list)

    def test_menu_detail_url_is_resolved(self):
        url = reverse('menu:menu_detail', args=[5])
        self.assertEquals(resolve(url).func, menu_detail)

    def test_item_detail_url_is_resolved(self):
        url = reverse('menu:item_detail', args=[5])
        self.assertEquals(resolve(url).func, item_detail)

    def test_create_new_menu_url_is_resolved(self):
        url = reverse('menu:menu_new')
        self.assertEquals(resolve(url).func, create_new_menu)

    def test_edit_menu_url_is_resolved(self):
        url = reverse('menu:menu_edit', args=[5])
        self.assertEquals(resolve(url).func, edit_menu)
