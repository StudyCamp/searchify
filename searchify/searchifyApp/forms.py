from django import forms
from django.forms import ModelForm
from .models import Post, Tag, User

class SnapCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image',)

class tagCreationForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)

class searchForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)

class contentSearchForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

class findForm(ModelForm):
    class Meta:
        model = User
        fields = ('username',)



