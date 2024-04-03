"""
URL configuration for healwiseweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import*



urlpatterns = [
    path('admin/', admin.site.urls),
     
        path('', about,name='about'),
        path('introduction/',introduction,name='introduction'),
        path('about/', us,name='us'),
        path('service/', service,name='service'),
        path('minor/',minor,name='minor'),
        path('appointmenthospital/',appointmenthospital,name='appointmenthospital'),
        path('intermediate/',intermediate,name='intermediate'),
        path('severe/',severe,name='severe'),
        path('question_general/',question_general,name='question_general'),
        path('que_gynac/',que_gynac,name='que_gynac'),
        path('que_orthopedist/',que_orthopedist,name='que_orthopedist'),
        path('que_ent/',que_ent,name='que_ent'),
        path('que_skin/',que_skin,name='que_skin'),
        path('que_dentist/',que_dentist,name='que_dentist'),
        path('review/',review,name='review'),
        path('singup/',singup,name='singup'),
        path('login/',login,name='login'),
        path('submit_appointment/', submit_appointment, name='submit_appointment'),
        path('profile/',profile,name='profile'),
        path('logout/', logout_view, name='logout'),
        path('appointmenthome/', submit_appointment, name='appointmenthome'),





        
        


]
