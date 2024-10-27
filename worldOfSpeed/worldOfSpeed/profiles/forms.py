from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('first_name', 'last_name', 'profile_picture',)


class ProfileCreateForm(ProfileBaseForm):
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.CharField(help_text='Age requirement: 21 years and above.')


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'

    password = forms.CharField(widget=forms.PasswordInput)