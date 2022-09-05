from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("logout/",views.logout1,name="logout"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("employye/",views.employye,name="employye"),
    path("e_show/",views.e_show,name="e_show"),
    path("e_show/",views.e_show,name="e_show"),
    path("v_register/",views.v_register,name="v_register"),
    path("v_route/",views.v_route,name="v_route"),
    path("v_maintenance/",views.v_maintenance,name="v_maintenance"),
    path("v_vmo/",views.v_vmo,name="v_vmo"),
    path("v_readings/",views.v_readings,name="v_readings"),
    path("m_city/",views.m_city,name="m_city"),
    path("m_route/",views.m_route,name="m_route"),
    path("m_stop/",views.m_stop,name="m_stop"),
    path("m_sessions/",views.m_sessions,name="m_sessions"),
    path("m_professions/",views.m_professions,name="m_professions"),


    # students urls
    path("s_Accounts/",views.s_Accounts,name="s_Accounts"),
    path("s_transport_user/",views.s_transport_user,name="s_transport_user"),
    path("s_fee_defaulters/",views.s_fee_defaulters,name="s_fee_defaulters"),
    path("s_fee_verified/",views.s_fee_verified,name="s_fee_verified"),
    path("s_registeration_request/",views.s_registeration_request,name="s_registeration_request"),
    path("s_update_reg_request/",views.s_update_reg_request,name="s_update_reg_request"),
    path("s_account_update/",views.s_account_update,name="s_account_update"),
    

    # Activate accounts
    path("activate_account_link/",views.activate_account_link,name="activate_account_link"),

    # email activation url
    path("activate/<uidb64>/<token>",views.activate,name="activate"),


    
    path("email_rejction_verification/",views.email_rejction_verification,name="email_rejction_verification"),



    # pdf reports
    path("downloadroutes/",views.downloadroutes,name="downloadroutes"),




]
