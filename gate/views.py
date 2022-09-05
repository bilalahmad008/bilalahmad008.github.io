from django.shortcuts import render
from home.models import vistors , vehicle_reading
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# login function
def index(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user=authenticate(username=username,password=password)


        if  user.is_superuser:
            messages.add_message(request, messages.INFO, 'invalid username or password')
            return HttpResponseRedirect('/8084/')

        if  user.is_staff:
            login(request, user)
            messages.add_message(request, messages.INFO, 'Login Succesfully')
            return HttpResponseRedirect('/8084/addvistors')
        else:
            messages.add_message(request, messages.INFO, 'invalid username or password')
            return HttpResponseRedirect('/8084')
    return render(request, "gate/login.html" ,)

def logout1(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logout Succesfully')
    return HttpResponseRedirect('/8084')



@login_required
def addvistors(request):
    current_user=request.user
    if  current_user.is_staff:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allinvistors = vistors.objects.filter(outtime=None)  
    context ={'task':allinvistors }
    if request.method == "POST":
        name=request.POST.get('name')
        cnic=request.POST.get('cnic')
        purpose=request.POST.get('purpose')        
        data = vistors(name=name,cnic=cnic,purpose=purpose )
        data.save()
        messages.add_message(request, messages.INFO, 'Vistor Data Added Successfully')
        return HttpResponseRedirect('/8084/addvistors')

    return render(request, "gate/addvisitors.html" ,context)

@login_required
def veheclein(request):
    current_user=request.user
    if  current_user.is_staff:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allvehicle=vehicle_reading.objects.filter(inreading=None)
        # modaldata=vehicle_reading.objects.filter(id=srno)
    return render(request, "gate/veheclein.html", {'allvehicle':allvehicle})

@login_required
def visitordetails(request):
    current_user=request.user
    if  current_user.is_staff:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    allvistors = vistors.objects.all()
    return render(request, "gate/visitordetails.html" ,{'allvistors':allvistors})



@login_required
def Task(request):
    current_user=request.user
    if  current_user.is_staff:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    return render(request, 'gate/view.html')

    
@login_required
def update(request):
    current_user=request.user
    if  current_user.is_staff:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    srno=request.POST.get('srno')
    vmodata=vehicle_reading.objects.filter(id=srno)
    tempid=""
    tempvno=""
    tempoutr=""
    for i in vmodata:
        tempid=i.id
        tempvno=i.vmoid
        tempoutr=i.outreading
    if request.POST.get("accepted") is not None and request.POST.get("accepted") == str("accepted"):
        Sr=request.POST.get('Sr')
        innreading=request.POST.get('innreading')
        inndate=request.POST.get('inndate')
        inntime=request.POST.get('inntime')
        vehicle_reading.objects.filter(id=Sr).update(inreading=innreading , indate=inndate , intime=inntime)
        messages.add_message(request, messages.INFO, 'Vehicle Reading Updated Successfully')
        return HttpResponseRedirect('/8084/veheclein/')


    return render(request, 'gate/update.html', {'tempid':tempid , 'tempvno':tempvno , 'tempoutr':tempoutr})

    

@login_required
def outvistorinsertion(request):
    current_user=request.user
    if  current_user.is_staff:
        print('ok')
    else:
        logout(request)
        messages.add_message(request, messages.INFO, 'Mera Putr apni console ty chal')
        return HttpResponseRedirect('/')
    vid=request.POST.get('vid')
    time = datetime.now()
    vistors.objects.filter(id=vid).update(outtime=time)    
    messages.add_message(request, messages.INFO, 'Vistor Data Out Successfully')
    return HttpResponseRedirect('/8084/addvistors')