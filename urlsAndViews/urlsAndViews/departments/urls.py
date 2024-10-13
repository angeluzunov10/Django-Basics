from django.urls import path, re_path, include

from urlsAndViews.departments.views import index, view_with_name, view_with_integer, view_with_slug, show_archive, \
    redirect_to_softuni, redirect_to_view

urlpatterns = [
    path('', index),
    path('redirect-to-view', redirect_to_view),
    path('softuni/', redirect_to_softuni),
    path('numbers/', include([
        path('<int:pk>/', view_with_integer),
        path('<int:pk>/<slug:slug>/', view_with_slug),
    ])),
    path('<variable>/', view_with_name),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', show_archive),
    path('<path:variable>', view_with_name),
    #path('<uuid:id>', some_view),
]