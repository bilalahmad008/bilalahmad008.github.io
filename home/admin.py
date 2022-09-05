from django.contrib import admin
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
from home.models import registration 
from home.models import challan 
from home.models import sessions 
from home.models import professions 
from import_export.admin import ImportExportModelAdmin



# # Register your models here.
admin.site.register(emp_personal)
admin.site.register(emp_medical)
admin.site.register(emp_emergency)
admin.site.register(emp_education)
admin.site.register(emp_courses)
admin.site.register(emp_experience)
admin.site.register(emp_job)
admin.site.register(Register_Vehicle)
admin.site.register(route)
admin.site.register(maintenance)
admin.site.register(vmo)
admin.site.register(vehicle_reading)
admin.site.register(citty)
admin.site.register(routte)
admin.site.register(sttop)
admin.site.register(registration)
admin.site.register(challan)
admin.site.register(sessions)
admin.site.register(professions)


@admin.register(Accounts_Data)
class userdat(ImportExportModelAdmin):
    pass