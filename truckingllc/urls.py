from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('quote/', views.quote_view, name='quote'),
    path('quote/success/', views.quote_success_view, name='quote_success'),
]
