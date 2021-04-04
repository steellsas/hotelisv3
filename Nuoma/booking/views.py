from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from rooms.models import Room
from .models import Reservation
from .forms import AddReserveDayForm

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
            total_price = 0
            advans = 0
            res = Reservation(user_id=useris,
                              room_id=room,
                              start_day=cd['start_day'],
                              end_day=cd['end_day'],
                              total=total_price,
                              advance=advans
            )
            range_day = count_day_range(res)
            res.advance = room.price
            res.total = count_total(range_day, room.price)
            # res.save()
            return render(request, 'accountas/created.html', {'res': 'res' })
    else:
        form = AddReserveDayForm()
        return render(request, 'hotel/rooms/detail.html', {'form': form})


def update_status(request, res_id):

    reservation =get_object_or_404(Reservation, pk=res_id)
    reservation.status = 1
    reservation.save()
    return redirect('dashboard')


def show_calendar(request):
    my_month =date.today().month
    start_year = date.today().year
    cal = HTMLCalendar().formatmonth(start_year, my_month)
    return render(request, 'mycalendar.html', {'my_calendar': cal})

#
# def calendar(request, year='2021', month='01'):
#   my_workouts = Workouts.objects.order_by('my_date').filter(
#     my_date__year=year, my_date__month=month
#   )
#   cal = WorkoutCalendar(my_workouts).formatmonth(year, month)
#   return render_to_response('mycalendar.html, {'calendar': mark_safe(cal)})

# -------------------- calendar for test
#
# class QuerysetCalendar(HTMLCalendar):
#
#     def __init__(self, queryset, field):
#         self.field = field
#         super(QuerysetCalendar, self).__init__()
#         self.queryset_by_date = self.group_by_day(queryset)
#
#     def formatday(self, day, weekday):
#         if day != 0:
#             cssclass = self.cssclasses[weekday]
#             if date.today() == date(self.year, self.month, day):
#                 cssclass += ' today'
#             if day in self.queryset_by_date:
#                 cssclass += ' filled'
#                 body = ['<ul>']
#
#                 for item in self.queryset_by_date[day]:
#                     body.append('<li>')
#                     body.append('<a href="%s">' % item.get_absolute_url())
#                     body.append(esc(item))
#                     body.append('</a></li>')
#                 body.append('</ul>')
#                 return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
#             return self.day_cell(cssclass, day)
#         return self.day_cell('noday', ' ')
#
#
#     def formatmonth(self, year, month):
#         self.year, self.month = year, month
#         return super(QuerysetCalendar, self).formatmonth(year, month)
#
#     def group_by_day(self, queryset):
#         field = lambda item: getattr(item, self.field).day
#         return dict(
#             [(day, list(items)) for day, items in groupby(queryset, field)]
#         )
#
#     def day_cell(self, cssclass, body):
#         return '<td class="%s">%s</td>' % (cssclass, body)
#
#
#
