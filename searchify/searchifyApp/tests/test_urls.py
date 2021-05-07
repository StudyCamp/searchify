from django.test import SimpleTestCase
from django.urls import reverse, resolve
from searchifyApp.views import index, find, userlist, profile, result, contentResult, search, searchTag, searchContent, create, login_view, logout_view, register

class TestUrls(SimpleTestCase):
    # Match URLs with their views functions
    def test_index_url_resolved(self):
        url = reverse('searchifyApp:index')
        self.assertEquals(resolve(url).func, index)

    def test_find_url_resolved(self):
        url = reverse('searchifyApp:find')
        self.assertEquals(resolve(url).func, find)

    def test_userlist_url_resolved(self):
        url = reverse('searchifyApp:userlist', args=['substring test'])
        self.assertEquals(resolve(url).func, userlist)

    def test_profile_url_resolved(self):
        url = reverse('searchifyApp:profile', args=['testUser'])
        self.assertEquals(resolve(url).func, profile)

    def test_result_url_resolved(self):
        url = reverse('searchifyApp:result', args=['tagSearch'])
        self.assertEquals(resolve(url).func, result)

    def test_contentResult_url_resolved(self):
        url = reverse('searchifyApp:contentResult', args=['contentSearch'])
        self.assertEquals(resolve(url).func, contentResult)

    def test_search_url_resolved(self):
        url = reverse('searchifyApp:search')
        self.assertEquals(resolve(url).func, search)

    def test_searchTag_url_resolved(self):
        url = reverse('searchifyApp:searchTag')
        self.assertEquals(resolve(url).func, searchTag)

    def test_searchContent_url_resolved(self):
        url = reverse('searchifyApp:searchContent')
        self.assertEquals(resolve(url).func, searchContent)

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