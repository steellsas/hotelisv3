from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('booking/<int:room_id>/', views.reservation_create, name='reservation_create'),
    path('calendar/', views.show_calendar, name='my_calender'),
    # path('add/<int:room_id>/', views.cart_add, name='cart_add'),
    path('update/<int:res_id>/', views.update_status, name='update_status'),
    path('paided/<int:res_id>/', views.update_status_paid, name='update_status_paid'),
    path('testmail/', views. test_share, name=' test_share')
]


