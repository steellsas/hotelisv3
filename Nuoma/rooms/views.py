from django.shortcuts import render, get_object_or_404
from rooms.models import Room, Category, RoomImage
from booking.forms import AddReserveDayForm,ReservationForm


def get_room_id(object):
    list_id = []
    for item in object:
      list_id.append(item.id)
    return list_id


def room_list(request, category_slug=None):
    category = None

    categories = Category.objects.all()
    rooms = Room.objects.filter(visible=True)
    imag = RoomImage.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        rooms = Room.objects.filter(category=category,  visible=True)

    return render(request,
                  'hotel/rooms/list.html',
                  {'category': category,
                   'categories': categories,
                   'rooms': rooms})


def room_detail(request, id, slug):

    room = get_object_or_404(Room,
                             id=id,
                             slug=slug,
                             visible=True)

    imags = RoomImage.objects.filter(room_id=room.id)
    prop = room.properties1.all()
    reservation_days = AddReserveDayForm()
    un_lst = ["2021-04-01", "2021-04-10", "2021-04-03", "2021-04-11"]



    return render(request,
                  'hotel/rooms/detail.html',
                  {'room': room,
                   'imags': imags,
                   'reservation_days': reservation_days,
                   'prop': prop,
                   'mydate': un_lst
                   })

