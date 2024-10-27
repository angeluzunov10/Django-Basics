from django.urls import path

from common.views import HomePage, DashboardPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('dashboard/', DashboardPage.as_view(), name='dashboard')
]