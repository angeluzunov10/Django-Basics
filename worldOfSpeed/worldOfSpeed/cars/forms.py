from django import forms

from cars.models import Car
from worldOfSpeed.mixins import ReadOnlyFieldsMixin, DisabledFieldsMixin


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    class Meta(CarBaseForm.Meta):
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }
        exclude = ['owner',]


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(DisabledFieldsMixin, ReadOnlyFieldsMixin, CarBaseForm):
    readonly_fields = ['model', 'year', 'image_url', 'price']
    disabled_fields = ['type']