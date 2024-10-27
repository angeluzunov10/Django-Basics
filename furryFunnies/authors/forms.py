from django import forms

from authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorCreateForm(AuthorBaseForm):
    class Meta():
        model = Author
        exclude = ('info', 'image_url',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name...',
                'label': 'First Name:'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name...',
                'label': 'Last Name:'
            }),
            'passcode': forms.PasswordInput(attrs={
                'placeholder': 'Enter 6 digits...',
                'label': 'Passcode:'
            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...',
                'label': 'Pets Number:'
            })
        }


class AuthorEditForm(AuthorBaseForm):
    class Meta():
        model = Author
        exclude = ('passcode',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'label': 'First Name:'
            }),
            'last_name': forms.TextInput(attrs={
                'label': 'Last Name:'
            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...',
                'label': 'Pets Number:'
            }),
            'info': forms.TextInput(attrs={
                'label': 'Info:'
            }),
            'image_url': forms.URLInput(attrs={
                'label': 'Profile Image URL:'
            }),
        }