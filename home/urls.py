from django.contrib import admin
from django.urls import path
from home import views

from django.views.static import serve 


urlpatterns = [
    path("", views.home, name='home'),
    path("medicalDiag", views.medicalDiag, name='medicalDiag'),
    path("physiobot", views.physiobot, name='physiobot'),
    path("support", views.support, name='support'),
    path("about", views.about, name='about'),
    path("report", views.report, name='report')
]
