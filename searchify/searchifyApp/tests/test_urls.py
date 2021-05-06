from django.test import SimpleTestCase
from django.urls import reverse, resolve
from searchifyApp.views import index, create, login_view, logout_view, register

class TestUrls(SimpleTestCase):

    def test_index_url_resolved(self):
        url = reverse('searchifyApp:index')
        self.assertEquals(resolve(url).func, index)

    def test_create_url_resolved(self):
        url = reverse('searchifyApp:share')
        self.assertEquals(resolve(url).func, create)

    def test_login_view_url_resolved(self):
        url = reverse('searchifyApp:login')
        self.assertEquals(resolve(url).func, login_view)
    
    def test_logout_view_url_resolved(self):
        url = reverse('searchifyApp:logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_register_url_resolved(self):
        url = reverse('searchifyApp:register')
        self.assertEquals(resolve(url).func, register)