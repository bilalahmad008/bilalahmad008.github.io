from asyncio.windows_events import NULL
from ipaddress import ip_address
from multiprocessing import context
from multiprocessing.sharedctypes import Value
from string import Template
from unicodedata import name
from urllib import response
from django import template
from django.shortcuts import render ,redirect , HttpResponse 
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http.response import HttpResponseRedirect
from django.contrib import messages



# user authentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# email activation 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.utils.encoding import force_bytes 
from django.utils.encoding import force_str
from django.core.mail import EmailMessage , send_mail
from . tokens import generate_token
from django.contrib.auth import authenticate , login , logout




from Students import settings


# # import database
from home.models import emp_personal
from home.models import emp_medical
from home.models import emp_emergency
from home.models import emp_education
from home.models import emp_courses
from home.models import emp_experience
from home.models import emp_job
from home.models import Register_Vehicle
from home.models import route
from home.models import maintenance
from home.models import vmo
from home.models import vehicle_reading
from home.models import citty
from home.models import routte
from home.models import sttop
from home.models import Accounts_Data


# students module
from home.models import registration
from home.models import challan
from home.models import sessions
from home.models import professions
# login function
def index(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user=authenticate(username=username,password=password)
        

        if  user.is_superuser:
            login(request, user)
            messages.add_message(request, messages.INFO, 'Login Succesfully')
            return HttpResponseRedirect('/8080/dashboard')
        else:
            messages.add_message(request, messages.INFO, 'invalid username or password')
            return HttpResponseRedirect('/8080/')
    return render(request, "home/login.html" ,)

# logout
def logout1(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logout Succesfully')
    return HttpResponseRedirect('/8080/')


def dashboard(request):
    return render(request , "home/dashboard.html")

@login_required
def employye(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    # personal
    if request.method == "POST":
        emp_id=request.POST.get('emp_id')
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        cnic=request.POST.get('cnic')
        ph1=request.POST.get('ph1')
        ph2=request.POST.get('ph2')
        email=request.POST.get('email')
        city=request.POST.get('city')
        adress=request.POST.get('adress')
        postal_code=request.POST.get('postal_code')
        marital_status=request.POST.get('marital_status')
        designation=request.POST.get('designation')
        image=request.FILES.get('image')
        Employee = emp_personal(emp_id=emp_id,name=name , fname =fname , gender=gender , dob=dob , cnic = cnic , ph1 = ph1 ,ph2=ph2,email=email,city=city,adress=adress,postal_code=postal_code,marital_status=marital_status , designation=designation,image=image)
        Employee.save()




        # emergency
        name_emergency=request.POST.get('name_emergency')
        relation_emergency=request.POST.get('relation_emergency')
        adress_emergency=request.POST.get('adress_emergency')
        city_emergency=request.POST.get('city_emergency')
        email_emergency=request.POST.get('email_emergency')
        ph1_emergency=request.POST.get('ph1_emergency')
        ph2_emergency=request.POST.get('ph2_emergency')
        Emp_emergency = emp_emergency(emp_id=emp_id,name=name_emergency , relation =relation_emergency , adress=adress_emergency , city=city_emergency , email=email_emergency , ph1=ph1_emergency , ph2=ph2_emergency )
        Emp_emergency.save()



        # medical
        blood_medical=request.POST.get('blood_medical')
        organ_doner_medical=request.POST.get('organ_doner_medical')
        disability_medical=request.POST.get('disability_medical')
        fitness_medical=request.POST.get('fitness_medical')
        Emp_medical = emp_medical(emp_id=emp_id,blood=blood_medical , organ_doner =organ_doner_medical , disability=disability_medical , fitness=fitness_medical )
        Emp_medical.save()


        # courses
        title_courses=request.POST.get('title_courses')
        institute_courses=request.POST.get('institute_courses')
        Duration_courses=request.POST.get('Duration_courses')
        date_of_complition_courses=request.POST.get('date_of_complition_courses')
        certificate_courses=request.POST.get('certificate_courses')
        no_of_project_courses=request.POST.get('no_of_project_courses')
        Emp_courses = emp_courses(emp_id=emp_id,title=title_courses , institute =institute_courses , Duration=Duration_courses , date_of_complition=date_of_complition_courses ,certificate=certificate_courses , no_of_project=no_of_project_courses )
        Emp_courses.save()



        # job details
        Designation_job=request.POST.get('Designation_job')
        job_description_job=request.POST.get('job_description_job')
        duty_time_job=request.POST.get('duty_time_job')
        Emp_job = emp_job(emp_id=emp_id,Designation=Designation_job , job_description =job_description_job , duty_time=duty_time_job)
        Emp_job.save()


        # expirence
        organization_expirence=request.POST.get('organization_expirence')
        adress_expirence=request.POST.get('adress_expirence')
        Designation_expirence=request.POST.get('Designation_expirence')
        joining_date_expirence=request.POST.get('joining_date_expirence')
        leaving_date_expirence=request.POST.get('leaving_date_expirence')
        Emp_experience = emp_experience(emp_id=emp_id,organization=organization_expirence , adress =adress_expirence , Designation=Designation_expirence , joining_date=joining_date_expirence , leaving_date = leaving_date_expirence )
        Emp_experience.save()


        # education
        title_education=request.POST.get('title_education')
        institute_education=request.POST.get('institute_education')
        board_education=request.POST.get('board_education')
        year_of_passing_education=request.POST.get('year_of_passing_education')
        persentage_education=request.POST.get('persentage_education')
        t_marks_education=request.POST.get('t_marks_education')
        o_marks_education=request.POST.get('o_marks_education')
        Emp_education = emp_education(emp_id=emp_id,title=title_education , institute =institute_education , board=board_education , year_of_passing=year_of_passing_education , persentage=persentage_education , t_marks=t_marks_education , o_marks=o_marks_education )
        Emp_education.save()
        messages.add_message(request, messages.INFO, 'Data Added Successfully')
        return HttpResponseRedirect('/8080/employye/')



    
    return render(request, "home/e_add.html")


@login_required
def e_show(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allTasks = emp_personal.objects.all()
    allTasks2 = emp_education.objects.all()
    allTasks3= emp_emergency.objects.all()
    allTasks4 = emp_medical.objects.all()
    allTasks5 = emp_courses.objects.all()
    allTasks6 = emp_experience.objects.all()
    allTasks7 = emp_job.objects.all()
    context ={'task':allTasks ,'task2':allTasks2  ,'task3':allTasks3  ,'task4':allTasks4  ,'task5':allTasks5  ,'task6':allTasks6  ,'task7':allTasks7}
    return render(request, "home/e_show.html" , context)



@login_required
def v_register(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allTasks = Register_Vehicle.objects.all()
    context ={'task':allTasks }
    if request.method == "POST":
        vehicleid=request.POST.get('vehicleid')
        brand=request.POST.get('brand')
        engine_no=request.POST.get('engine_no')
        body_no=request.POST.get('body_no')
        engine_pwr=request.POST.get('engine_pwr')
        colour=request.POST.get('colour')
        capsity=request.POST.get('capsity')
        date1=request.POST.get('date1')
   
        Registerr_Vehicle = Register_Vehicle(vehicleid=vehicleid,brand=brand , engine_no =engine_no , body_no=body_no , engine_pwr=engine_pwr , colour = colour , capsity=capsity , date1 = date1 )
        Registerr_Vehicle.save()
        messages.add_message(request, messages.INFO, 'Vehicle Added Successfully')
        return HttpResponseRedirect('/8080/v_register')
    return render(request, "home/v_register.html" , context)


@login_required
def v_route(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    downloadroute=routte.objects.all()
    allroute=route.objects.all()
    allvehicle=Register_Vehicle.objects.all()
    allcity=citty.objects.all()
    if request.method == "POST":
        if request.POST.get("city") is not None and request.POST.get("city") != str("Select Session") and request.POST.get("route") is not None and request.POST.get("route") != str("Select Route") and request.POST.get("stop") is not None and request.POST.get("stop") != str("") and request.POST.get("time") is not None and request.POST.get("time") != str(""):
            temp_rid=request.POST.get('rid')
            temp_city=request.POST.get('city')
            temp_routes=request.POST.get('route')
            temp_stop=request.POST.get('stop')
            temp_time=request.POST.get('time')
            Route=route( rid=temp_rid , city=temp_city , routes=temp_routes , stop= temp_stop, time=temp_time )
            Route.save()
            messages.add_message(request, messages.INFO, 'Data Added Successfully')


        city=request.POST.get("city")
        data=request.POST.get("route")
        if data != "Select Route" and not None:
            obj=citty.objects.filter(name=city).first()
            routee=routte.objects.filter(city=obj)
            temp=routte.objects.filter(name=data).first()
            stops=sttop.objects.filter(route=temp)
            flag=1
            return render(request,"home/v_route.html",{"city":city,"allcity":allcity , "allroute":allroute , "downloadroute":downloadroute ,"routee":routee,"stops":stops,"idnt":data , "allvehicle":allvehicle ,"flag":flag})

        obj=citty.objects.filter(name=city).first()
        routee=routte.objects.filter(city=obj)
        return render(request,"home/v_route.html",{"city":city,"allcity":allcity,"allroute":allroute , "downloadroute":downloadroute ,"routee":routee,"idnt":"Select Route" , "allvehicle":allvehicle})
    return render(request,"home/v_route.html",{"allcity":allcity, "allroute":allroute , "downloadroute":downloadroute,"city":"Select City",  "idnt":"Select Route" , "allvehicle":allvehicle})

    
@login_required
def v_maintenance(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allTasks = maintenance.objects.all()
    alldrivers = emp_personal.objects.filter(designation="Driver")
    allvehicles = Register_Vehicle.objects.all()
    allmechanics = emp_personal.objects.filter(designation="Mechanic")
    context ={'task':allTasks ,"alldrivers":alldrivers , "allvehicles":allvehicles , "allmechanics":allmechanics}
    if request.method == "POST":
        id=request.POST.get('id')
        driver_id=request.POST.get('driver_id')
        vid=request.POST.get('vid')
        meachanice_id=request.POST.get('meachanice_id')
        problem=request.POST.get('problem')
        workdone=request.POST.get('workdone')
        ewr=request.POST.get('ewr')
        date1=request.POST.get('date1')
   
        Maintenance = maintenance(id=id,driver_id=driver_id , vid =vid , meachanice_id=meachanice_id, problem=problem , workdone=workdone  , ewr=ewr  , date1=date1)
        Maintenance.save()
        messages.add_message(request, messages.INFO, 'Data Added Successfully')
        return HttpResponseRedirect('/8080/v_maintenance/')
    return render(request, "home/v_maintenance.html" , context)



@login_required
def v_vmo(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allTasks = vmo.objects.all()
    allTasks1 = emp_personal.objects.filter(designation="Driver")   
    allTasks2 = emp_personal.objects.filter(designation="Conductor")   
    allTasks3 = Register_Vehicle.objects.all()
    context ={'task':allTasks , 'task1':allTasks1,'task2':allTasks2 , "task3":allTasks3}
    if request.method == "POST":        
        vid =request.POST.get('vid')
        d1 =request.POST.get('d1')
        h1 =request.POST.get('h1')
        #emp_id=request.POST.get('emp_id')
        h2 =request.POST.get('h2')
        d2 =request.POST.get('d2')
        use=request.POST.get('use')
        station=request.POST.get('station')
        Submittedby =request.POST.get('Submittedby')
        recommendedby =request.POST.get('recommendedby')
        approvedby =request.POST.get('approvedby')
        Vmo=vmo(vid=vid, d1=d1, h1=h1, h2=h2, d2=d2, use=use, station=station,Submittedby=Submittedby, recommendedby=recommendedby, approvedby= approvedby )
        Vmo.save()

        #Table Vehicle in
        outdate =request.POST.get('outdate')
        outtime =request.POST.get('outtime')
        outreading =request.POST.get('outreading')
        Vehicle_reading=vehicle_reading(vmoid=vid,outdate=outdate,outtime=outtime,outreading=outreading)
        Vehicle_reading.save()
        messages.add_message(request, messages.INFO, 'Data Added Successfully')
        return HttpResponseRedirect('/8080/v_vmo/')
    return render(request, "home/v_vmo.html" , context)



@login_required
def v_readings(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allreadings=vehicle_reading.objects.all()
    return render(request, "home/v_readings.html" , {'allreadings':allreadings} )

# studnet functions
@login_required
def s_Accounts(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    all_accounts=Accounts_Data.objects.all()
    return render(request, "home/s_Accounts.html",{"all_accounts":all_accounts} )


@login_required
def s_transport_user(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    all_registers=registration.objects.all()
    return render(request, "home/s_transport_user.html",{"all_registers":all_registers} )

@login_required
def s_fee_defaulters(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    all_registers=registration.objects.filter(status="Defaulter")
    return render(request, "home/s_fee_defaulters.html",{"all_registers":all_registers} )

@login_required
def s_registeration_request(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    all_registers=challan.objects.filter(status="pending")
    return render(request, "home/s_registeration_request.html",{"all_registers":all_registers} )

@login_required
def s_fee_verified(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    all_registers=registration.objects.filter(status="verified")
    return render(request, "home/s_fee_verified.html",{"all_registers":all_registers} )

@login_required
def s_account_update(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    if request.POST.get("acceptdata") is not None and request.POST.get("acceptdata") == str("accepted"):
        tempuser =request.POST.get('tempuser')
        tempfirstnamee =request.POST.get('tempfirstnamee')
        templastnamee =request.POST.get('templastnamee')
        tmpemail =request.POST.get('tmpemail')
        Accounts_Data.objects.filter(username=tempuser).update(first_name=tempfirstnamee , last_name=templastnamee, email=tmpemail)
        messages.add_message(request, messages.INFO, 'User Account Updated Successfully')
        return HttpResponseRedirect('/8080/s_Accounts/')

    tempusername =request.POST.get('tempusername')
    tempfirstname =request.POST.get('tempfirstname')
    templastname =request.POST.get('templastname')
    tempemail =request.POST.get('tempemail')
              
    return render(request, "home/s_account_update.html" ,{'tempusername':tempusername, 'tempfirstname':tempfirstname , 'templastname':templastname  , 'tempemail':tempemail})




@login_required
def s_update_reg_request(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    rigid =request.POST.get('rigid')
    session =request.POST.get('session')
    regdata=challan.objects.filter( rigid=rigid ,session=session )
    if request.POST.get("acceptdata") is not None and request.POST.get("acceptdata") == str("accepted"):
        temmrigid =request.POST.get('rerigid')
        temmsession =request.POST.get('resession')
        paid_amount =request.POST.get('paid_amount')
        remaining_amount =request.POST.get('remaining_amount')

        challan.objects.filter(rigid=temmrigid , session=temmsession).update(status="paid" , paid_amount=paid_amount , remaining_amount=remaining_amount)
        registration.objects.filter(rigid=temmrigid).update(status="verified")
        messages.add_message(request, messages.INFO, 'Challan Updated Successfully')
        return HttpResponseRedirect('/8080/s_registeration_request/')

    temp_regnum=""
    temp_session=""
    temp_paid=""
    temp_remaining=""
    for i in regdata:
        temp_regnum=i.rigid
        temp_session=i.session
        temp_paid=i.paid_amount
        temp_remaining=i.remaining_amount        
    return render(request, "home/s_update_reg_request.html" ,{'regdata':regdata, 'temp_regnum':temp_regnum , 'temp_session':temp_session  , 'temp_paid':temp_paid , 'temp_remaining':temp_remaining})

@login_required
def activate_account_link(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    tempusername =request.POST.get('tempusername')
    tempfirstname =request.POST.get('tempfirstname')
    templastname =request.POST.get('templastname')
    tempemail =request.POST.get('tempemail')
    temppassword =request.POST.get('temppassword')
    userexit=""
    if User.objects.filter(username=tempusername):
        myuser=User.objects.get(username=tempusername)
        User.objects.filter(username=tempusername).update(password=temppassword)     
        
        myuser.is_active =False
        myuser.save()
        messages.add_message(request, messages.INFO, 'Account Reactivated! Please Activate from the email you recieved.')

        #     # welcome Email
        # subject="Welcome to CUI Transport Department-Login"
        # message="Hello " + tempfirstname +"!! \n" + "Welcome to Comsats Transport Department!! \n" + "\n \n"+ " if you doesn't recieve activation account link email, please check the span box of your email \n" + "Regards \n" +"Chaudhary Bilal Ahmad"
        # from_email=settings.EMAIL_HOST_USER
        # to_list=[tempemail]
        # send_mail(subject , message ,from_email , to_list , fail_silently=True)

        # Email Address Configration Email
        current_site = get_current_site(request)
        

        email_subject="Confirm your Email @ CUI - TRANSPORT LOGIN !!"
        message2 = render_to_string('home/email_confirmation.html' , {
            'username':tempusername,
            'password':temppassword,
            'name':tempfirstname, 
            'domain':current_site.domain , 
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser),
                })
        email=EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
            )
                
        email.fail_silently=True
        email.send()
        
    else:
        myuser=User.objects.create_user(tempusername,tempemail,temppassword)     
        myuser.first_name=tempfirstname
        myuser.last_name=templastname
        myuser.is_active =False
        myuser.save()
        messages.add_message(request, messages.INFO, 'Account created! Please Activate from the email you recieved.')

        #     # welcome Email
        # subject="Welcome to CUI Transport Department-Login"
        # message="Hello " + tempfirstname +"!! \n" + "Welcome to Comsats Transport Department!! \n" + "\n \n"+ " if you doesn't recieve activation account link email, please check the span box of your email \n" + "Regards \n" +"Chaudhary Bilal Ahmad"
        # from_email=settings.EMAIL_HOST_USER
        # to_list=[tempemail]
        # send_mail(subject , message ,from_email , to_list , fail_silently=True)

        # Email Address Configration Email
        current_site = get_current_site(request)
        

        email_subject="Confirm your Email @ CUI - TRANSPORT LOGIN !!"
        message2 = render_to_string('home/email_confirmation.html' , {
            'username':tempusername,
            'password':temppassword,
            'name':tempfirstname, 
            'domain':current_site.domain , 
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser),
                })
        email=EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
            )
                
        email.fail_silently=True
        email.send()


    
    

    
    # return HttpResponseRedirect('/')
    return render(request, "home/s_Accounts.html")

@login_required
def email_rejction_verification(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    rigid =request.POST.get('deleterequest')
    tempsession =request.POST.get('session')

    
    myyuser=Accounts_Data.objects.filter(username=rigid)
    useremail=""
    userfname=""
    for i in myyuser:
        useremail=i.email
        userfname=i.first_name

    # Rejection Email
    subject="Welcome to CUI Transport Department"
    message="Hello " + userfname +"!! \n" + "Welcome to Comsats Transport Department!! \n" + "\n \n"+ " Comsats Transport Depardment Reject Your Challan Request due to not clear challan image or wrong challan image.  \n" +"\n\n"+"Please Login to your CUI Transport Console to Resend Your Challan \n" + "Regards \n" +"Chaudhary Bilal Ahmad"
    from_email=settings.EMAIL_HOST_USER
    to_list=[useremail]
    send_mail(subject , message ,from_email , to_list , fail_silently=True)
    pi = challan.objects.get(rigid=rigid , session=tempsession)
    pi.delete()
    messages.add_message(request, messages.INFO, 'Rejected and Sent Mail Successfully')
    return HttpResponseRedirect('/8080/s_registeration_request/')


# Activation account email
@login_required
def activate(request, uidb64, token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        myuser=User.objects.get(pk=uid)
    except(TypeError , ValueError , OverflowError , User.DoesNotExist):
        myuser=None
    
    if myuser is not None and generate_token.check_token(myuser , token):
        myuser.is_active=True
        myuser.save()
        # login(request , myuser)
        return render(request , 'home/activation_pass.html')

    else:
        return render(request , 'home/activation_fail.html')


# add minor
@login_required
def m_city(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allTasks = citty.objects.all()
    context ={'task':allTasks }
    if request.method == "POST":
        name=request.POST.get('name')
   
        City = citty(name=name )
        City.save()
        messages.add_message(request, messages.INFO, 'Data Added Successfully')
        return HttpResponseRedirect('/8080/m_city/')
    return render(request, "home/m_city.html" , context)

@login_required
def m_sessions(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allsessions = sessions.objects.all()
    context ={'task':allsessions }
    if request.method == "POST":
        name=request.POST.get('name')
   
        Sessions = sessions(session=name )
        Sessions.save()
        messages.add_message(request, messages.INFO, 'Data Added Successfully')
        return HttpResponseRedirect('/8080/m_sessions/')
    return render(request, "home/m_sessions.html" , context)

@login_required
def m_professions(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allsessions = professions.objects.all()
    context ={'task':allsessions }
    if request.method == "POST":
        name=request.POST.get('name')
   
        Professions = professions(professionz=name )
        Professions.save()
        messages.add_message(request, messages.INFO, 'Data Added Successfully')
        return HttpResponseRedirect('/8080/m_professions/')
    return render(request, "home/m_professions.html" , context)



@login_required
def m_route(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    alldrivers=emp_personal.objects.filter(designation="Driver")
    allconductor=emp_personal.objects.filter(designation="Conductor")
    allvehicle=Register_Vehicle.objects.all()
    allTasks = citty.objects.all()
    allsession = sessions.objects.all()
    allTasks1 = routte.objects.all()
    context ={ 'allsession':allsession, 'task':allTasks , 'task1':allTasks1 , "allvehicle":allvehicle , "v_id":"Select Vehicle" , "name":"" , "city":"Select City" , "alldrivers":alldrivers , "allconductor":allconductor , "conductor":"Select conductor" , "driver":"Select Driver" , "driverph":"" , "conductorph":"" , "session":"Select Session"}
    if request.method == "POST":
        city=request.POST.get('city')
        name=request.POST.get('name')
        session=request.POST.get('session')
        v_id=request.POST.get('v_id')
        conductor=request.POST.get('conductor')
        driver=request.POST.get('driver')
        tempconductorph=emp_personal.objects.filter(name=conductor)
        tempdriverph=emp_personal.objects.filter(name=driver)
        driverph=""
        conductorph=""
        for i in tempconductorph:
            conductorph=i.ph1
        for i in tempdriverph:
            driverph=i.ph1
        if request.POST.get("city") is not None and request.POST.get("city") != str("Select City") and request.POST.get("session") is not None and request.POST.get("session") != str("Select Session") and request.POST.get("v_id") is not None and request.POST.get("v_id") != str("Select Vehicle") and request.POST.get("driver") is not None and request.POST.get("driver") != str("Select Driver") and request.POST.get("driver_ph1") is not None and request.POST.get("driver_ph1") != str("") and request.POST.get("conductor") is not None and request.POST.get("conductor") != str("Select conductor") and request.POST.get("conductor_ph") is not None and request.POST.get("conductor_ph") != str("") and request.POST.get("name") is not None and request.POST.get("name") != str(""):
            tempcity=request.POST.get('city')
            tempsession=request.POST.get('session')
            tempv_id=request.POST.get('v_id')
            tempdriver=request.POST.get('driver')
            tempdriver_ph1=request.POST.get('driver_ph1')
            tempconductor=request.POST.get('conductor')
            tempconductor_ph=request.POST.get('conductor_ph')
            tempname=request.POST.get('name')
            Routte = routte(city=citty.objects.get(name=tempcity) , session=tempsession , v_id=tempv_id , driver= tempdriver, driver_ph1=tempdriver_ph1 , conductor=tempconductor , conductor_ph=tempconductor_ph ,name=tempname )
            Routte.save()
            messages.add_message(request, messages.INFO, 'Data Added Successfully')
            return HttpResponseRedirect('/8080/m_route/')
        return render(request, "home/m_route.html" , {'allsession':allsession , 'allvehicle':allvehicle, 'task':allTasks , 'task1':allTasks1 , "v_id":v_id , "city":city , "name":name , "alldrivers":alldrivers , "allconductor":allconductor , "conductor":conductor  ,"driver":driver , "driverph":driverph , "conductorph":conductorph , "session":session})
    return render(request, "home/m_route.html" , context)

@login_required
def m_stop(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allcity=citty.objects.all()
    allstops=sttop.objects.all()
    if request.method == "POST":
        city=request.POST.get("city")
        obj=citty.objects.filter(name=city).first()
        route=routte.objects.filter(city=obj)
        if request.POST.get("stop") is not None and request.POST.get("stop") != str(""):
            sav_route=request.POST.get('route')
            sav_stop=request.POST.get('stop')
            Routee=sttop(name=sav_stop, route=routte.objects.get(name=sav_route))
            Routee.save()
            messages.add_message(request, messages.INFO, 'Route Added Successfully')
            return redirect("m_stop")

                

            


        return render(request,"home/m_stop.html",{"city":city,"allcity":allcity,"route":route,"idnt":"Select Route" , "allstops":allstops })

    return render(request,"home/m_stop.html",{"allcity":allcity,"city":"Select City","idnt":"Select Route" , "allstops":allstops})









# pdf reports 
# 1.Route pdf
@login_required
def downloadroutes(request):
    current_user=request.user
    if  current_user.is_superuser:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
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
        Template_path='home/route_report.html'
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition']='filename="route.pdf"'
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

     





