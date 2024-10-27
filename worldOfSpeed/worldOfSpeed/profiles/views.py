from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from cars.models import Car
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.mixins import ProfileObjectMixin
from profiles.models import Profile
from worldOfSpeed.utils import get_user_obj


class ProfileCreatePage(CreateView):
    model = Profile
    template_name = 'profiles/profile-create.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('cars-catalogue')


class ProfileDetailsPage(ProfileObjectMixin, DetailView):
    template_name = 'profiles/profile-details.html'


class ProfileEditPage(ProfileObjectMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('profile-details')


class ProfileDeletePage(ProfileObjectMixin, DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')
