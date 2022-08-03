from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import flight,passengers
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,"flights/index.html",{
        "flights":flight.objects.all()
    })

def Flight(request,flight_id):
    Flight=flight.objects.get(pk=flight_id)
    return render(request,"flights/flight.html",{
        "flight":Flight,
        "passengers":Flight.passengers.all()
    })
  

def book(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method=="POST":
            passenger=passengers()
            flight_id=int(request.POST["flight"])
            flights=flight.objects.get(pk=flight_id)
            passenger.first=request.POST["passengers1"]
            passenger.last=request.POST["passengers2"]
            passenger.id=request.POST["id"]
            passenger.save()
            flights.save()
            passenger.flight.add(flights)
            return HttpResponseRedirect(reverse("flight",args=(flight_id,)))
        else:
            return render(request,"flights/book.html",{
                "Flights":flight.objects.all()
            })

def login_book(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("book"))
        else:
            return render(request,"flights/login.html",{
                "message":"error in password or username"
            })
    else:
        return render(request,"flights/login.html")


def logout_book(request):
    logout(request)
    return render(request, "flights/login.html", {
        "message": "Logged out."
    })

def signup(request):
    pass

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1!=password2:
            return render(request, "flights/register.html", {
                "message": "Passwords must match."
            })
        try:
            user=User.objects.create_user(username, email, password1)
            user.save()
        except IntegrityError:
            return render(request, "flights/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"flights/register.html")


    
