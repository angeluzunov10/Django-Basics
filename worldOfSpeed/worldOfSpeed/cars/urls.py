from django.urls import path

from cars.views import CarCreatePage, CarsCataloguePage, CarDetailsPage, CarEditPage, CarDeletePage

urlpatterns = [
    path('create/', CarCreatePage.as_view(), name='create-car'),
    path('catalogue/', CarsCataloguePage.as_view(), name='cars-catalogue'),
    path('<int:id>/details/', CarDetailsPage.as_view(), name='car-details'),
    path('<int:id>/edit/', CarEditPage.as_view(), name='car-edit'),
    path('<int:id>/delete/', CarDeletePage.as_view(), name='car-delete'),
]