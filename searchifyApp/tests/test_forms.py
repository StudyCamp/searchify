from django.test import SimpleTestCase
from searchifyApp.forms import SnapCreationForm, tagCreationForm, searchForm, contentSearchForm, findForm

class TestForm(SimpleTestCase):
    # Validation test for SnapCreationForm
    def test_SnapCreationForm_form_valid_data(self):
        form = SnapCreationForm(data={
            'content':'content2',
            'image':'image2',
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
    # No data error test for SnapCreationForm
    def test_SnapCreationForm_form_no_data(self):
        form = SnapCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
    # Tests for tagCreationForm
    def test_tagCreationForm_form_valid_data(self):
        form = tagCreationForm(data={
            'tag':'tag2'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
    
    def test_tagCreationForm_form_no_data(self):
        form = tagCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
    # Tests for searchForm
    def test_searchForm_form_valid_data(self):
        form = searchForm(data={
            'tag':'tag3'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_searchForm_form_no_data(self):
        form = searchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
    # Tests for contentSearchForm
    def test_contentSearchForm_form_valid_data(self):
        form = contentSearchForm(data={
            'content':'contentTest000'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_contentSearchForm_form_no_data(self):
        form = contentSearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    # Tests for findForm
    def test_findForm_form_valid_data(self):
        form = findForm(data={
            'name_user':'usernameTests'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_findForm_form_no_data(self):
        form = contentSearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)