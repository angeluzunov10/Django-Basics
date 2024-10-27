from django.urls import path

from profiles.views import ProfileCreatePage, ProfileDetailsPage, ProfileEditPage, ProfileDeletePage

urlpatterns = [
    path('create/', ProfileCreatePage.as_view(), name='create-profile'),
    path('details/', ProfileDetailsPage.as_view(), name='profile-details'),
    path('edit/', ProfileEditPage.as_view(), name='profile-edit'),
    path('delete/', ProfileDeletePage.as_view(), name='profile-delete')
]
