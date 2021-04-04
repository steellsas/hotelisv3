from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

apps_name = 'account'

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('staff/', views.dashboard, name='staff_dashboard'),
    path('', include('django.contrib.auth.urls')),
    # path('log/', views.login_view, name='custom_login' ),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

]