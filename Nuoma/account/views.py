
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from booking.models import Reservation




@login_required
def dashboard(request):
    user =request.user
    profile = get_object_or_404(Profile, user=user)
    reserve = Reservation.objects.filter(user_id=user)

    return render(request, 'account/dashboard.html', {'section': 'dashboard',
                                                      'profile': profile,
                                                      'rezervations': reserve})