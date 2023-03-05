from django.shortcuts import render, redirect
from datetime import datetime
from .models import Contact
from django.contrib import messages
from .forms import DP_uploader, username_updater


def index(request):
    if request.user.is_authenticated:
        tour_list = request.user.tours.all()
        context = {'tour_list': tour_list}
        return render(request, 'tour/index.html', context)
    else:
        context = {}
        return render(request, 'tour/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Successfully Submitted!")
    return render(request, 'tour/contact.html')


def pastTours(request):
    return render(request, 'tour/index.html')


def profile(request):
    return render(request, 'tour/profile.html')


def update_dp(request):
    if request.method == "POST":
        dp_form = DP_uploader(request.POST, request.FILES,
                              instance=request.user.profile)
        if dp_form.is_valid():
            dp_form.save()
            messages.success(request, "Successfully Updated")

    else:
        dp_form = DP_uploader(instance=request.user.profile)
    context = {
        'dp_form': dp_form
    }
    return render(request, 'tour/update_dp.html', context)


def update_username(request):
    if request.method == "POST":
        u_form = username_updater(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Successfully Updated")

    else:
        u_form = username_updater(instance=request.user)
    context = {
        'u_form': u_form
    }
    return render(request, 'tour/update_username.html', context)
