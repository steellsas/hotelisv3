from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.room_list, name= 'room_list'),
    path('<slug:category_slug>/', views.room_list, name='room_list_by_category'),
    path('<int:id>/<slug:slug>/', views.room_detail, name='room_detail'),

]

