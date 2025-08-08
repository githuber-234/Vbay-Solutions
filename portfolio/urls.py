from django.urls import path
from .views import (HomeView, ServicesView, AboutView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
]