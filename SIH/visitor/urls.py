from django.contrib import admin
from django.urls import path,include

from.import views
 

urlpatterns=[
    path("CL",views.CL,name="CL"),
    path("CLR",views.CLR,name="CLR"),
    path("MLR",views.MLR,name="MLR"),
    path("WLR",views.WLR,name="WLR"),
    path("TLR",views.TLR,name="TLR"),

]