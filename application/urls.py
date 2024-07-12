from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base'),  # Replace `views.index` with your desired view function
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    # Other URL patterns as needed
]
