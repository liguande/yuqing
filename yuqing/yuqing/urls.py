"""yuqing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from yuqingApp import views as yuqingApp_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',yuqingApp_views.index,name="home"),
    url(r'^create_user/$',yuqingApp_views.create,name="create_user"),
    url(r'^new_user/$',yuqingApp_views.new,name="new_user"),
    url(r'^login/$',yuqingApp_views.login,name="login"),
    url(r'^login_session$',yuqingApp_views.login_session,name="login_session"),
    url(r'^welcome/$',yuqingApp_views.welcome,name="welcome"),
]
