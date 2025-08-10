from django.urls import path
from .views import (HomeView, ServicesView, AboutView, PortfolioView,
                    BlogView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', PortfolioView.as_view(), name='portfolio'),
    path('blog/', BlogView.as_view(), name='blog'),
]