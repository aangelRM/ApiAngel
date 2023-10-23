"""
URL configuration for APIANGEL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from api.views import *
from api import views

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('forgot-password/', Forgot_password.as_view(), name='forgot_password'),
    path('recover-password/', Recover_password.as_view(), name='recover_password'),
    path('index/', Main.as_view(), name='main'),
    path('index/', Home1.as_view(), name='home1'),
    path('index2/', Home2.as_view(), name='home2'),
    path('index3/', Home3.as_view(), name='home3'),
    path('widgets/', Widgets.as_view(), name='widgets'),
    path('registarUsuario/', FormularioUsuarioView.index, name="registarUsuario"),
    path('guardarUsuario/', FormularioUsuarioView.procesar_formulario, name="guardarUsuario"),
    

    
]