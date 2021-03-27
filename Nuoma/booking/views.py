from django.shortcuts import render,get_object_or_404, redirect
from .forms import AddReserveDayForm
from .models import Reservation
from rooms.models import Room
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import Reservation


def count_day_range(object):

    y = object.start_day.year
    m = object.start_day.month
    d = object.start_day.day

    y1 = object.end_day.year
    m1 = object.end_day.month
    d1 = object.end_day.day

    dd = date(y, m, d)
    d2 = date(y1, m1, d1)

    delta = d2 - dd
    return delta.days


def count_total(range_of_days, day_price):
    return range_of_days * day_price


@login_required()
def reservation_create(request, room_id):

    # if request.user.is_authenticated:
    # if request.method == 'POST':
    useris = request.user
    room = get_object_or_404(Room, id=room_id)
    form = AddReserveDayForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        total_price = 0
        advans = 0
        res = Reservation(user_id=useris,
                          room_id=room,
                          start_day=cd['start_day'],
                          end_day = cd['end_day'],
                          total = total_price,
                          advance=advans
        )
        range_day = count_day_range(res)
        res.advance = room.price
        res.total = count_total(range_day, room.price)
        res.save()

        return render(request, 'accountas/created.html', {'res': 'res' })




