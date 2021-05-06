from django.test import TestCase, Client
from django.urls import reverse
from searchifyApp.models import Post, Tag, User
from searchifyApp.forms import SnapCreationForm, tagCreationForm, searchForm

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('searchifyApp:index')
        self.create_url= reverse('searchifyApp:share')
        self.search_url= reverse('searchifyApp:search')
        # Objects creation for testing
        self.user1 = User.objects.create(
            username='user1',
            password='password1',
        )
        self.post1 = Post.objects.create(
            content='content1',
            poster=self.user1,
            image='image1.png'
        )
        self.post2 = Post.objects.create(
            content='content2',
            poster=self.user1,
            image='image2.png',
        )

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchifyApp/index.html')

    def test_create_GET(self):
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchifyApp/create.html')

    def test_search_GET(self):
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchifyApp/search.html')
    
    def test_result_GET(self):
        self.result_url = reverse('searchifyApp:result', kwargs={'tag':'test123'})
        response = self.client.get(self.result_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchifyApp/result.html')
    
    def test_profile_GET(self):
        # User not found, 404.
        self.profile_url = reverse('searchifyApp:profile', kwargs={'username':'404usernotfound'})
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 404)
        # User found, 200.
        self.profile_url = reverse('searchifyApp:profile', kwargs={'username':'user1'})
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchifyApp/profile.html')
        
    def test_create_form_(self):
        form = SnapCreationForm(data= {
        'content':'testCreate',
        'poster':self.user1,
        'timestamp':'1',
        'image':'imageTest.png'
        })
        self.assertEqual(form.data["content"], 'testCreate')
      
    def test_search_form_(self):
        form = searchForm(data= {
            'tag':'testTag'
        })
        self.assertEqual(form.data["tag"], 'testTag')

    def test_create_POST_adds_new_tag(self):
        self.post1.tagged_posts.create(
            tag = 'tag1',
        )
        response = self.client.post(self.create_url)        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.post1.tagged_posts.first().tag, 'tag1')

    def test_search_POST(self):
        self.post1.tagged_posts.create(
            tag = 'tag1',
        )
        self.post1.tagged_posts.create(
            tag = 'tag2',
        )
        self.post2.tagged_posts.create(
            tag = 'tag2',
        )
        response = self.client.post(self.search_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.post1.tagged_posts.last().tag, 'tag2')
        self.assertEquals(self.post2.tagged_posts.first().tag, 'tag2')
        count = Post.objects.filter(tagged_posts__tag='tag2').count()
        self.assertEquals(count, 2)

  

