from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furryFunnies.utils import get_user_obj
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts.models import Post


class CreatePostPage(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class DetailsPostPage(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/details-post.html'


class EditPostPage(UpdateView):
    model = Post
    form_class = PostEditForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.get_object().__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class DeletePostPage(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.get_object().__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
