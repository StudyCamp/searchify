from django import forms
from django.forms import ModelForm
from .models import Post, Tag, User

# Use for uploading image with content 
class SnapCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image',)

# Use for including tags for the image being uploaded
class tagCreationForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)

# Use for searching images by tags
class searchForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)

# Use for searching content by tags
class contentSearchForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

# Use for searching users/profiles by sub/string
class findForm(forms.Form):
    name_user = forms.CharField(max_length=100)


