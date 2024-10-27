from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from authors.forms import AuthorCreateForm, AuthorEditForm
from authors.mixins import ProfileObjectMixin
from authors.models import Author


class AuthorCreatePage(CreateView):
    model = Author
    template_name = 'authors/create-author.html'
    form_class = AuthorCreateForm
    success_url = reverse_lazy('dashboard')


class AuthorDetailsPage(ProfileObjectMixin, DetailView):
    template_name = 'authors/details-author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        last_updated_post = author.posts.order_by('-updated_at').first()
        context['last_updated_post'] = last_updated_post
        return context


class AuthorEditPage(ProfileObjectMixin, UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['author'] = Author.objects.first()
        return content


class AuthorDeletePage(ProfileObjectMixin, DeleteView):
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('home')




