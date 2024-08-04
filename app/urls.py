from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('student/', student, name='student'),
    path('studentRequest/', studentRequest, name='studentRequest'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('volunteer/', volunteer, name='volunteer'),
    path('volunteerRequest/', volunteerRequest, name='volunteerRequest'),
    path('companion/<int:pk>', companion, name='companion'),
    path('info/', info, name='info'),
    path('settings/', settings, name='settings'),
]
