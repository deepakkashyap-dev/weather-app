from django.urls import path
from django.contrib import admin
from dashboard import views
from django.views.generic import RedirectView
from django.urls import re_path

urlpatterns = [
    path("",views.index,name="Home"),
    path("login",views.loginUser,name="Login"),
    path("logout",views.logotUser,name="Logout"),
    re_path(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='catch-all-redirect'),
]