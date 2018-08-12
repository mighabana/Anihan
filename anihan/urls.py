"""anihan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from webapp.views import *

app_name= 'webapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', render_home),
    url(r'^login/$', render_login, name="login"),
    url(r'^login/process/$', process_login),
    url(r'^signup/$', render_signup, name="signup"),
    url(r'^signup/process/$', process_signup),
    url(r'^order/$', render_vegetables, name="order"),
    url(r'^order/submit/$', submit_order),
    url(r'^order/vegetables/$', render_vegetables),
    url(r'^order/fruits/$', render_fruits),
    url(r'^order/livestock/$', render_livestock),
    url(r'^order/poultry/$', render_poultry),
    url(r'^order/fisheries/$', render_fisheries),
    url(r'^order/grains/$', render_grains),
    url(r'^init_db/$', init_db),
    url(r'^dashboard/$', render_dashboard, name="dashboard")
]
