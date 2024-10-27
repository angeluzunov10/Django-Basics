from django.urls import path

from authors.views import AuthorCreatePage, AuthorDetailsPage, AuthorEditPage, AuthorDeletePage

urlpatterns = [
    path('create/', AuthorCreatePage.as_view(), name='create-author'),
    path('details/', AuthorDetailsPage.as_view(), name='details-author'),
    path('edit/', AuthorEditPage.as_view(), name='edit-author'),
    path('delete/', AuthorDeletePage.as_view(), name='delete-author'),
]