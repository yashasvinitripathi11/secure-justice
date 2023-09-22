from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

from.import views
 

urlpatterns=[
    path("visitor",views.CL,name="CL"),
    path("CLR",views.CLR,name="CLR"),
    path("MLR",views.MLR,name="MLR"),
    path("WLR",views.WLR,name="WLR"),
    path("TLR",views.TLR,name="TLR"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

