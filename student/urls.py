from django.contrib import admin
from django.urls import path 
from student import views

urlpatterns = [
    path("",views.index,name="login"),
    path("login/",views.index,name="login"),
    path("logout/",views.logout1,name="logout"),
    path("signup/",views.signup,name="signup"),
    path("home/",views.home1,name="home"),
    path("uploadchallan/",views.uploadchallan,name="uploadchallan"),

    path("route/",views.route1,name="route"),
    path("card/",views.card,name="card"),

    path("registration/",views.reg,name="registration"),


    # routes pdf download
    path("downloadroutes/",views.downloadroutes,name="downloadroutes"),

]
