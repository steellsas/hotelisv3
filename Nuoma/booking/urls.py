from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('booking/<int:room_id>/', views.reservation_create, name='reservation_create'),
    # path('add/<int:room_id>/', views.cart_add, name='cart_add'),
    # path('remove/<int:room_id>/', views.cart_remove, name='cart_remove'),
]


