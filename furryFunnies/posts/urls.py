from django.urls import path

from posts.views import CreatePostPage, DetailsPostPage, EditPostPage, DeletePostPage

urlpatterns = [
    path('create/', CreatePostPage.as_view(), name='create-post'),
    path('<int:post_id>/details/', DetailsPostPage.as_view(), name='details-post'),
    path('<int:post_id>/edit/', EditPostPage.as_view(), name='edit-post'),
    path('<int:post_id>/delete/', DeletePostPage.as_view(), name='delete-post'),
]