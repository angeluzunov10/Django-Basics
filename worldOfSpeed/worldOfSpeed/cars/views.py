from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from cars.models import Car
from worldOfSpeed.utils import get_user_obj


class CarsCataloguePage(ListView):
    model = Car
    fields = '__all__'
    template_name = 'cars/catalogue.html'


class CarCreatePage(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('cars-catalogue')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CarDetailsPage(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'cars/car-details.html'


class CarEditPage(UpdateView):
    model = Car
    form_class = CarEditForm
    pk_url_kwarg = 'id'
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('cars-catalogue')


class CarDeletePage(DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    pk_url_kwarg = 'id'
    form_class = CarDeleteForm
    success_url = reverse_lazy('cars-catalogue')

    def get_initial(self):
        return self.get_object().__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

