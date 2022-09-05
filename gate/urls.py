from django.contrib import admin
from django.urls import path 
from gate import views

urlpatterns = [
    path("",views.index,name="home"),
    path("logout/",views.logout1,name="logout"),
    path("addvistors",views.addvistors,name="addvistors"),
    path("veheclein/",views.veheclein,name="veheclein"),
    path("visitordetails/",views.visitordetails,name="visitordetails"),
     path("login/",views.login,name="login"),
     path("outvistorinsertion/",views.outvistorinsertion,name="outvistorinsertion"),
     path("update/",views.update,name="update"),
]
