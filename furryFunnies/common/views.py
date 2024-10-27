from django.views.generic import TemplateView, ListView
from posts.models import Post


class HomePage(TemplateView):
    template_name = 'common/index.html'


class DashboardPage(ListView):
    model = Post
    fields = '__all__'
    template_name = 'common/dashboard.html'
