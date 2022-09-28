from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('Home/', views.Home),
    path('companyhome.html', views.companyhome),
    path('Management.html', views.Management),
    path('manageuser.html', views.manageusers),
    path('Newdeveloper.html', views.Dev_add),
    path('Newteamlead.html', views.TL_add),
    path('DUpdate/', views.D_Update),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('TLUpdate/', views.TL_Update),
    path('edit1/<int:id>', views.ed),
    path('delete1/<int:id>', views.delt),
    path('Manager.html', views.Manager_login),
    path('Teamlead.html', views.TL_login),
    path('Teamleadspace.html', views.TL_space),
    path('viewreport/', views.report),
    path('approve/<int:id>/', views.approve),
    path('Assignwork.html', views.Assign_work),
    path('Developer.html', views.Dev_login),
    path('approvedreport.html', views.approved_report),
    path('Developermanu.html', views.Dev_home),
    path('viewwork.html', views.view_work),
    path('report.html', views.the_report),
]