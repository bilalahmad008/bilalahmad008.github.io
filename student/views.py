from django.contrib import messages
from django.shortcuts import render
from datetime import datetime
from django.http.response import HttpResponseRedirect
import os
from django.conf import settings
from django.http import HttpResponse, Http404
# from math import ceil
from home.models import professions, registration , challan
from home.models import citty
from home.models import sttop
from home.models import route
from home.models import routte
from home.models import sessions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa

date=datetime.now()
# Create your views here.

def index(request):
    if request.method == "POST":
        username=request.POST.get('username')
        username=username.upper()
        password=request.POST.get('password') 
        last_name="Student"
        user=authenticate(username=username,password=password , last_name=last_name)

        if user is not None:
            if  user.is_superuser:
                messages.add_message(request, messages.INFO, 'invalid username or password')
                return HttpResponseRedirect('/8082')
            else:
                messages.add_message(request, messages.INFO, 'Login Succesfully')
                login(request, user)
                return HttpResponseRedirect('/8082/home')
        else:
            messages.add_message(request, messages.INFO, 'invalid username or password')
            return HttpResponseRedirect('/8082/')
    return render(request, "student/login.html")


def logout1(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logout Succesfully')
    return HttpResponseRedirect('/8082/')
    

# def home1(request):
#     return render(request, "home.html")
@login_required
def home1(request):
    current_user=request.user
    if  current_user.is_superuser:
        logout(request)
        messages.add_message(request, messages.INFO, 'invalid username or password')
        return HttpResponseRedirect('/8082')
    # if request.method == 'POST':
    #     if reg_sign_up.objects.filter(rid=request.POST['rid'], cnic=request.POST['cnic']).exists():
    #         login = reg_sign_up.objects.get(rid=request.POST['rid'], cnic=request.POST['cnic'])
    #         return render(request, 'home.html', {'veriable': login})
    #     else:
    #         context = {'msg': 'Invalid Registration number or CNIC'}
    #         return render(request, 'login.html', context)
    return render(request, "student/home.html")

def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        email=request.POST.get('email')
        last_name=request.POST.get('last_name') 
        pass1=request.POST.get('pass1')  
        pass2=request.POST.get('pass2')     
        
        if User.objects.filter(username=username):
            messages.add_message(request, messages.INFO, 'User Already Exist!')
        if len(username)>10:
            messages.add_message(request, messages.INFO, 'UserName must under 10 characters!')

        if len(username)>12:
            messages.add_message(request, messages.INFO, 'UserName must under 10 characters!')
        if pass1 != pass2:
            messages.add_message(request, messages.INFO, 'Password does not Match')
        else:
            myuser=User.objects.create_user(username,email,pass1)     
            myuser.first_name=first_name
            myuser.last_name=last_name
            myuser.save()
            messages.add_message(request, messages.INFO, 'User Created Successfully')
            return HttpResponseRedirect('//8082/')
        

        
        
        
    return render(request, "student/signup.html")


@login_required
def route1(request):
    allroutes=routte.objects.all()
  
    return render(request, "student/route.html",{'allroutes':allroutes})

@login_required
def card(request):
    current_user=request.user
    user_name=current_user.username
    allTasks = registration.objects.filter(rigid=user_name).all()   
    context ={'task':allTasks}
    return render(request, "student/card.html",context) 

@login_required
def reg(request):
    current_user=request.user
    user_name=current_user.username
    full_name=current_user.first_name
    temp_prof=current_user.last_name
    namesess=sessions.objects.last()
    temp_session=namesess.session
    flag=0
    if registration.objects.filter(rigid=user_name , session1=temp_session):
        flag=1
        
    allcity=citty.objects.all()
    if request.method == "POST":
        if request.POST.get("uni_hostel_resident") is not None and request.POST.get("uni_hostel_resident") != str("University Hostel Residence") and request.POST.get("city") is not None and request.POST.get("city") != str("")  and request.POST.get("route") is not None and request.POST.get("route") != str("")  and request.POST.get("stop") is not None and request.POST.get("stop") != str("")  and request.POST.get("adress") is not None and request.POST.get("adress") != str("")  and request.POST.get("ph") is not None and request.POST.get("ph") != str("")  and request.POST.get("emergency_ph") is not None and request.POST.get("emergency_ph") != str("") and request.POST.get("date1") is not None and request.POST.get("date1") != str(""):
            rigid=request.POST.get('rigid')
            name=request.POST.get('name')
            session=request.POST.get('session')
            profession1=request.POST.get('profession')
            uni_hostel_resident=request.POST.get('uni_hostel_resident')
            city1=request.POST.get('city')
            route1=request.POST.get('route')
            stop1=request.POST.get('stop')
            adress=request.POST.get('adress')
            ph=request.POST.get('ph')
            emergency_ph=request.POST.get('emergency_ph')
            date1=request.POST.get('date1')
            image1=request.FILES.get('image1')
            if registration.objects.filter(rigid=rigid , session1=temp_session):
                messages.add_message(request, messages.INFO, 'Already Uploaded')
                return HttpResponseRedirect('/8082/registration/', {'user_name':user_name , 'full_name':full_name , 'temp_prof':temp_prof , 'temp_session':temp_session , 'flag':flag})

            else:
                Registration = registration(rigid=rigid,name=name,session1=session,profession=profession1 , uni_hostel_resident =uni_hostel_resident , city=city1 , route=route1 , stop = stop1 , adress = adress ,ph=ph,emergency_ph=emergency_ph,date1=date1,image1=image1)
                Registration.save()
                messages.add_message(request, messages.INFO, 'Data Added Successfully') 
                return HttpResponseRedirect('/8082/registration/', {'user_name':user_name , 'full_name':full_name , 'temp_prof':temp_prof , 'temp_session':temp_session , 'flag':flag})

        city=request.POST.get("city")
        data=request.POST.get("route")
        uni_residence=request.POST.get("uni_hostel_resident")
        if data != "Select Route" and not None:
            obj=citty.objects.filter(name=city).first()
            route=routte.objects.filter(city=obj)
            temp=routte.objects.filter(name=data).first()
            stops=sttop.objects.filter(route=temp)
         
            return render(request,"student/registration.html",{"city":city,"allcity":allcity,"route":route,"stops":stops,"idnt":data , 'user_name':user_name , 'full_name':full_name , 'temp_prof':temp_prof , 'temp_session':temp_session , 'flag':flag , 'uni_residence':uni_residence})

        obj=citty.objects.filter(name=city).first()
        route=routte.objects.filter(city=obj)
        return render(request,"student/registration.html",{"city":city,"allcity":allcity,"route":route,"idnt":"Select Route" , 'user_name':user_name , 'full_name':full_name , 'temp_prof':temp_prof , 'temp_session':temp_session , 'flag':flag , 'uni_residence':uni_residence})
    return render(request,"student/registration.html",{"allcity":allcity,"city":"Select City","idnt":"Select Route" , 'user_name':user_name , 'full_name':full_name , 'temp_prof':temp_prof , 'temp_session':temp_session , 'flag':flag , 'uni_residence':'University Hostel Residence'} )

@login_required
def uploadchallan(request):
    namesess=sessions.objects.last()
    temp_session=namesess.session
    current_user=request.user
    user_name=current_user.username
    pendingchallan=challan.objects.filter(rigid=user_name ,session=temp_session , status='pending')
    allfees=challan.objects.filter(rigid=user_name , session=temp_session , status="paid")
    flaagg=0
    fllaagg=0
    if challan.objects.filter(rigid=user_name ,session=temp_session , status='pending'):
        flaagg=2 
    if challan.objects.filter(session=temp_session , status='paid'):
        flaagg=3
    if request.POST.get("update") is not None and request.POST.get("update") == str("updation"): 
        fllaagg=1
        flaagg=3
    context ={'pendingchallan':pendingchallan ,'allfees':allfees ,'user_name':user_name  ,'temp_session':temp_session , 'flaagg':flaagg , 'fllaagg':fllaagg}


    
    if  request.POST.get("challanupload") is not None and request.POST.get("challanupload") == str("challanuploaded") : 
        rigid=request.POST.get('rigid')
        sesionn=request.POST.get('sesionn')
        image1=request.FILES.get('image1')
        if challan.objects.filter(rigid=rigid , session=temp_session) :
            print(temp_session)
            # challan.objects.filter(rigid=rigid , session=sesionn).update(image=image1)
            messages.add_message(request, messages.INFO, 'updated succesfully')
            return HttpResponseRedirect('/8082/uploadchallan/',{'fllaagg':fllaagg})
        else:
            Challan = challan(rigid=rigid,image=image1 , session=sesionn)
            Challan.save()
            messages.add_message(request, messages.INFO, 'Data Added Successfully')
            return HttpResponseRedirect('/8082/uploadchallan/')

        

    
    return render(request, "student/uploadchallan.html" , context)





# pdf reports 
@login_required
def downloadroutes(request):
    if request.method == "POST":
        routename=request.POST.get('routename')
        allTasks = route.objects.filter(routes=routename)
        busdata = routte.objects.filter(name=routename)
        drivername=""
        driverph=""
        conductorname=""
        conductorph=""
        vehicleno=""
        session=""
        for i in busdata:
            drivername=i.driver
            driverph=i.driver_ph1
            conductorname=i.conductor
            conductorph=i.conductor_ph
            vehicleno=i.v_id
            session=i.session
        context ={'task':allTasks ,"busdata":busdata , "routename":routename , "drivername":drivername , "driverph":driverph , "conductorname":conductorname , "conductorph":conductorph , "vehicleno":vehicleno ,"session":session}
        Template_path='student/route_report.html'
        response=HttpResponse(content_type='route/pdf')
        response['Content-Disposition']='filename="student/emp_report.pdf"'
        template=get_template(Template_path)
        html=template.render(context)
        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response )
        # if error then show some funy view
        if pisa_status.err:
           return HttpResponse('We had some errors <pre>' + html + '</pre>' )
        return response
    return HttpResponse('We had some errors please try later <pre>' + '</pre>' )
