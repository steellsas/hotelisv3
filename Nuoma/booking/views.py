from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from rooms.models import Room
from .models import Reservation
from .forms import AddReserveDayForm, TestEmailForm


from django.core.mail import send_mail
from django.http import HttpResponse

import calendar
from calendar import HTMLCalendar
from datetime import date


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

# redirect_field_name=''
@login_required()
def reservation_create(request, room_id):

    if request.method == 'POST':
        useris = request.user
        room = get_object_or_404(Room, id=room_id)
        form = AddReserveDayForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            dates= cd['date_range'].split(' - ')
            total_price = 0
            advans = 0
            star_d = datetime.strptime(dates[0], '%Y-%m-%d')
            star_n = datetime.strptime(dates[1], '%Y-%m-%d')
            res = Reservation(user_id=useris,
                              room_id=room,
                              start_day= star_d,
                              end_day=star_n,
                              total=total_price,
                              advance=advans
            )
            range_day = count_day_range(res)
            res.advance = room.price
            res.total = count_total(range_day, room.price)
            res.save()
            return render(request, 'accountas/created.html', {'res': 'res' })
    else:
        form = AddReserveDayForm()
        return render(request, 'hotel/rooms/detail.html', {'form': form})


def update_status(request, res_id):
    print(status =request.POST)
    reservation =get_object_or_404(Reservation, pk=res_id)
    reservation.status = 0

    subject= 'hello'
    message ='Rezervacija patvirtinta'
    send_mail(subject, message, 'aplienius@gmail.com',
              ['aplienius@gmail.com'])

    reservation.save()

    return redirect('dashboard')


def update_status_paid(request, res_id):
    if request.method =='POST':

        reservation =get_object_or_404(Reservation, pk=res_id)
        reservation.status = 2
        # send mail   reservation is booked  paid send order with reservation
        subject = 'hello'
        message = 'Uzsakymas priimtas, apmoketas'
        send_mail(subject, message, 'aplienius@gmail.com',
              ['aplienius@gmail.com'])
        reservation.save()

    return redirect('dashboard')


def show_calendar(request):
    my_month =date.today().month
    start_year = date.today().year
    cal = HTMLCalendar().formatmonth(start_year, my_month)
    pirmas= request.session['room_id']
    return render(request, 'mycalendar.html', {'my_calendar': cal, 'tet':pirmas})


# _________________________  testform  book/testmail


def test_share(request):
    sent = False
    if request.method =='POST':

        form = TestEmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #send mail
            subject = f"{cd['name']} recommends you read "
            message =  f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'aplienius@gmail.com',
                      [cd['to']])
            sent = True

    else:
        form = TestEmailForm()

    return render(request, 'test_email.html', {'form': form, 'sent': sent})


