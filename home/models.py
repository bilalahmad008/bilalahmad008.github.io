
from django.db import models
from datetime import datetime

class emp_personal(models.Model):
    emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
    name= models.CharField(max_length=50,null=False)
    fname=models.CharField(max_length=50,null=False)
    gender=models.CharField(max_length=15,null=False)
    dob=models.DateField(null=False)
    cnic=models.BigIntegerField(null=False)
    ph1=models.BigIntegerField(null=False)
    ph2=models.BigIntegerField(null=False)
    email=models.CharField(max_length=50,null=False)
    city=models.CharField(max_length=50,null=False)
    adress=models.CharField(max_length=100,null=False)
    postal_code=models.IntegerField(null=False)
    marital_status=models.CharField(max_length=50,null=False)
    designation=models.CharField(max_length=50,null=False)
    image = models.FileField(upload_to="employee/image")

    class Meta:
        db_table="emp_personal"




class emp_medical(models.Model):
        
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        blood=models.CharField(max_length=3, null=False)
        organ_doner= models.CharField(max_length=10, null=False)
        disability= models.CharField(max_length=10, null=False)
        fitness= models.CharField(max_length=10, null=False)
        class Meta:
            db_table="emp_medical"



class emp_emergency(models.Model):
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        name=models.CharField(max_length=20, null=False)
        relation=models.CharField(max_length=20, null=False)
        adress=models.CharField(max_length=50, null=False)
        city=models.CharField(max_length=20, null=False)
        email=models.CharField(max_length=25, null=False)
        ph1=models.BigIntegerField(null=False)
        ph2=models.BigIntegerField(null=False)
        class Meta:
            db_table="emp_emergency"


class emp_education(models.Model):
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        title=models.CharField(max_length=20, null=False)
        institute=models.CharField(max_length=20, null=False)
        board=models.CharField(max_length=10, null=False)
        year_of_passing=models.IntegerField(null=False)
        persentage=models.IntegerField(null=False)
        t_marks=models.IntegerField(null=False)
        o_marks=models.IntegerField(null=False)
        class Meta:
            db_table="emp_education"



class emp_courses(models.Model):
        
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        title=models.CharField(max_length=20, null=False)
        institute=models.CharField(max_length=20, null=False)
        Duration=models.CharField(max_length=10)
        date_of_complition=models.DateField(null=False)
        certificate=models.CharField(max_length=50 , null=False)
        no_of_project=models.IntegerField(null=False)
        class Meta:
            db_table="emp_courses"


class emp_experience(models.Model):
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        organization=models.CharField(max_length=100, null=False)
        adress=models.CharField(max_length=100)
        Designation=models.CharField(max_length=100, null=False)
        joining_date=models.DateField(null=False)
        leaving_date=models.DateField(null=False)
        class Meta:
            db_table="emp_experience"


class emp_job(models.Model):
    
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        Designation=models.CharField(max_length=100, null=False)
        job_description=models.CharField(max_length=100, null=False)
        duty_time=models.IntegerField(null=False)
        class Meta:
            db_table="emp_job"


# class student(models.Model):
        






# # vehicle database

class Register_Vehicle(models.Model):
        vehicleid= models.CharField(max_length=30,primary_key=True,null=False)
        brand=models.CharField(max_length=20, null=False)
        engine_no=models.CharField(max_length=30, null=False)
        body_no=models.CharField(max_length=40, null=False)
        engine_pwr=models.CharField(max_length=30, null=False)
        colour=models.CharField(max_length=30, null=False)
        capsity=models.CharField(max_length=30, null=False)
        date1=models.DateField(null=False)
        class Meta:
            db_table="Register_Vehicle"



class route(models.Model):
        rid =models.AutoField(primary_key=True,null=False) 
        routes=models.CharField(max_length=20, null=False)
        city=models.CharField(max_length=20, null=False)
        stop=models.CharField(max_length=20, null=False)
        time=models.CharField(max_length=20, null=False )
        class Meta:
            db_table="route"



class maintenance(models.Model):
        id= models.AutoField(primary_key=True)
        driver_id=models.CharField(max_length=100 , null=True)
        vid=models.CharField(max_length=100 , null=True)        
        meachanice_id=models.CharField(max_length=100,null=True) 
        problem=models.CharField(max_length=5000,null=True)
        workdone=models.CharField(max_length=5000,null=True)
        ewr=models.CharField(max_length=30 , null=False)
        date1=models.DateTimeField()     
        class Meta:
            db_table="maintenance"


class vmo(models.Model):
        id= models.AutoField(primary_key=True)
        vid=models.CharField(max_length=100,null=False)
        d1=models.CharField(max_length=100,null=False)
        h1=models.CharField(max_length=100,null=True)      
        d2=models.CharField(max_length=100,null=True)
        h2=models.CharField(max_length=100,null=True)
        use=models.CharField(max_length=500)
        station=models.CharField(max_length=200)
        Submittedby=models.CharField(max_length=100)
        recommendedby=models.CharField(max_length=100)
        approvedby=models.CharField(max_length=100)
        date=models.DateTimeField(default=datetime.now)
        class Meta:
            db_table="automobiles"

# Primary Key remove option
class vehicle_reading(models.Model):
        id=models.AutoField(primary_key=True)
        vmoid=models.CharField(max_length=100,null=False)
        outreading=models.IntegerField(null=False)
        outdate=models.DateField()
        outtime=models.TimeField()
        inreading=models.IntegerField(null=True)
        indate=models.DateField(null=True)
        intime=models.TimeField(null=True)
        empid=models.CharField(max_length=100,null=True)
        class Meta:
            db_table="vehicle_reading"







# Add minor
class citty(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class routte(models.Model):
    city= models.ForeignKey(citty ,max_length=100 , on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    session= models.CharField(max_length=50,null=False)
    v_id=models.CharField(max_length=20, null=False)
    driver=models.CharField(max_length=20, null=False)
    conductor=models.CharField(max_length=20, null=False)
    driver_ph1=models.BigIntegerField(null=False)
    conductor_ph=models.BigIntegerField(null=False)

    def __str__(self):
        return self.name



class sttop(models.Model):
    route= models.ForeignKey(routte ,max_length=100 , on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name


class sessions(models.Model):
        rid =models.AutoField(primary_key=True,auto_created=True) 
        session= models.CharField(max_length=50,null=False)
        class Meta:
            db_table="sessions"


class professions(models.Model):
        rid =models.AutoField(primary_key=True,auto_created=True) 
        professionz= models.CharField(max_length=50,null=False)
        class Meta:
            db_table="professions"






#transport users

class Accounts_Data(models.Model):
    
        username= models.CharField(max_length=50,null=False)
        first_name= models.CharField(max_length=50,default="pending")
        last_name= models.CharField(max_length=50,default="pending")
        password= models.CharField(max_length=50,default="pending")
        email= models.CharField(max_length=50,default="pending")

        class Meta:
            db_table="Accounts_Data"




# Students & Faculty Models

class registration(models.Model):
        # serial_no=models.CharField(primary_key=True)
        rigid=models.CharField(primary_key=True,max_length=100, null=False)
        name=models.CharField(max_length=100, null=True) 
        session1=models.CharField(max_length=60, null=True) 
        profession=models.CharField(max_length=50, null=False)
        uni_hostel_resident=models.CharField( max_length=50,null=False)
        city=models.CharField(max_length=50, null=False)
        route=models.CharField(max_length=20, null=False)
        stop=models.CharField(max_length=40, null=False)
        adress=models.CharField(max_length=100)
        ph=models.BigIntegerField(null=False)
        emergency_ph=models.BigIntegerField(null=False)
        date1=models.DateField(null=False)
        image1 = models.FileField(upload_to="student/image")
        status=models.CharField(max_length=100, default="Defaulter") 
        class Meta:
            db_table="registration_copy"
        


class challan(models.Model):
    
        rid =models.AutoField(primary_key=True,auto_created=True) 
        rigid= models.CharField(max_length=50,null=False)
        session= models.CharField(max_length=50,null=False)
        date1=models.DateTimeField(default=datetime.now) 
        status= models.CharField(max_length=50,default="pending")
        paid_amount= models.CharField(max_length=50,default="0")
        remaining_amount= models.CharField(max_length=50,default="0")
        image = models.ImageField(upload_to="student/image")

        class Meta:
            db_table="challan"






# gate models

class vistors(models.Model):
        id =models.AutoField(primary_key=True,null=False) 
        name= models.CharField(max_length=100,null=False)
        cnic=models.CharField(max_length=30, null=False)
        purpose=models.CharField(max_length=70, null=False)
        date1=models.DateTimeField(default=datetime.now) 
        outtime=models.TimeField(null=True)
        Refrence=models.CharField(max_length=100,null=True)
        class Meta:
            db_table="vistors"

