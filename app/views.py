from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User, auth


@login_required(login_url='/login')
def home(request):
    return render(request, 'base.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'volunteer.html')
        else:
            return render(request, 'loginnew.html')
    return render(request, 'loginnew.html')


def signup(request):
    return render(request, 'signup.html')


@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return render(request, 'loginnew.html')


@login_required(login_url='/login')
def studentRequest(request):
    if request.method == "POST":
        context = {}
        student1 = Student.objects.all().filter(User1=request.user)
        username = request.POST['volunteer']
        detail = Details.objects.all().filter(Name=username)
        volunteer1 = Volunteer.objects.all().filter(RollNumber=detail[0])
        volunteeruser = User.objects.all().filter(username=volunteer1[0].User1)
        # print(volunteeruser)
        volunteer = Volunteer.objects.all().filter(User1=1)  # initialisation, do not delete
        for i in volunteeruser:
            for j in Volunteer.objects.all().filter(User1=i):
                volunteer = j
        print(volunteer)
        for i in student1:
            Request.objects.create(
                Student=i,
                StudentArea=i.HomeArea,
                Volunteer=volunteer,
                StudentUser1=request.user,
                VolunteerUser1=volunteer.User1
            )
        context['Request'] = Request.objects.all().filter(StudentUser1=request.user)
        return render(request, 'studentRequest.html', {'context': context})
    return render(request, 'studentRequest.html')


@login_required(login_url='/login')
def student(request):
    if request.method == 'POST':
        context = {}
        area = request.POST['area']
        context['availableVolunteer'] = AvailableVolunteer.objects.all().filter(PickupArea=area)
        return render(request, 'student.html', {'context': context})
    return render(request, 'student.html')


@login_required(login_url='/login')
def companion(request, pk):
    context = {'companion': AvailableVolunteer.objects.all().filter(id=pk)}
    return render(request, 'companions.html', {'context': context})


@login_required(login_url='/login')
def volunteerRequest(request):
    context = {'Request': Request.objects.all().filter(VolunteerUser1=request.user)}
    return render(request, 'volunteerRequest.html', {'context': context})


@login_required(login_url='/login')
def volunteer(request):
    if request.method == 'POST':
        # print(request.POST)
        volunteer1 = Volunteer.objects.all().filter(User1=request.user)
        print(volunteer1)
        AvailableVolunteer.objects.create(
            Volunteer=volunteer1[0],
            PickupArea=request.POST['area'],
            Note=request.POST['note'],
            User1=request.user

        )
        return volunteerRequest(request)
    return render(request, 'volunteer.html')


@login_required(login_url='/login')
def info(request):
    context = {'Details': Details.objects.all().filter(User1=request.user)}
    return render(request, 'info.html', {'context': context})


@login_required(login_url='/login')
def settings(request):
    context = {'Details': Details.objects.all().filter(User1=request.user)}
    return render(request, 'settings.html', {'context': context})
