from django.test import SimpleTestCase
from searchifyApp.forms import SnapCreationForm, tagCreationForm

class TestForm(SimpleTestCase):

    def test_SnapCreationForm_form_valid_data(self):
        form = SnapCreationForm(data={
            'content':'content2',
            'image':'image2',
        })
        self.assertTrue(form.is_valid())

    def test_SnapCreationForm_form_no_data(self):
        form = SnapCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_tagCreationForm_form_valid_data(self):
        form = tagCreationForm(data={
            'tag':'tag2'
        })
        self.assertTrue(form.is_valid())