from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from booking.models import Reservation
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, ChangeStatus
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm


#
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request,user)
#             if 'next' in request.POST:
#                 return  redirect(request.POST.get('next'))
#             else:
#                 redirect('dashboard')
#     else:
#         form = AuthenticationForm()
#
#     return render(request, 'registration/login.html', {'form':form})


@login_required
def dashboard(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    reserve = Reservation.objects.filter(user_id=user)

    reserv = Reservation.objects.filter(status='0')
    acepted = Reservation.objects.filter(status='1')
    booked_res = Reservation.objects.filter(status='2')
    form = ChangeStatus()
    if user.is_staff:
        return render(request, 'account/owner_dashboard.html', {'profile': profile,
                                                                'all_build_res': reserv,
                                                                'all_acepted_res': acepted,
                                                                'booked_res': booked_res,
                                                                 'form':form

                                                                })
    else:
        return render(request, 'account/dashboard.html', {'section': 'dashboard',
                                                          'profile': profile,
                                                          'reservations': reserve})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile(user=new_user)
            profile.phone = user_form.cleaned_data['phone']
            # Profile.objects.create(user=new_user, commit=False)
            profile.save()

            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated ', 'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})