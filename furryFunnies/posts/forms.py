from django import forms

from furryFunnies.mixins import ReadOnlyMixin
from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateForm(PostBaseForm):
    class Meta():
        model = Post
        exclude = ('updated_at', 'author',)
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Put an attractive and unique title...',
                'label': 'Title:'
            }),
            'image_url': forms.URLInput(attrs={
                'label': 'Post Image URL:'
            }),
            'content': forms.TextInput(attrs={
                'placeholder': 'Share some interesting facts about your adorable pets...',
                'label': 'Content:'
            }),
        }


class PostEditForm(PostBaseForm):
    class Meta():
        model = Post
        exclude = ('updated_at', 'author',)
        widgets = {
            'title': forms.TextInput(attrs={
                'label': 'Title:'
            }),
            'image_url': forms.URLInput(attrs={
                'label': 'Post Image URL:'
            }),
            'content': forms.TextInput(attrs={
                'label': 'Content:'
            }),
        }


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    readonly_fields = ['title', 'image_url', 'content',]
    class Meta():
        model = Post
        exclude = ('updated_at', 'author',)
        widgets = {
            'title': forms.TextInput(attrs={
                'label': 'Title:'
            }),
            'image_url': forms.URLInput(attrs={
                'label': 'Post Image URL:'
            }),
            'content': forms.TextInput(attrs={
                'label': 'Content:'
            }),
        }
