from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("<int:flight_id>",views.Flight,name="flight"),
    path("book",views.book,name="book"),
    path("login",views.login_book,name="login"),
    path("logout",views.logout_book,name="logout"),
    path("register",views.register,name="register")
]