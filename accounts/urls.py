from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('products/', views.products_view, name='products'),
]
