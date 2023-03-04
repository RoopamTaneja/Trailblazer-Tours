from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'tour'
urlpatterns = [
    path('', views.index, name='tour_home'),
    path('contact/', views.contact, name='contact_page'),
    path('profile/',views.profile, name='profile'),
    path('profile/update_dp',views.update_dp, name = 'update_dp'),
    path('profile/update_username',views.update_username, name = 'update_username'),
    path('pastTours/', views.pastTours, name='pastTours'),
    path('polls/', include('polls.urls'))
]
