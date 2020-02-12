"""python_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from . import views

app_name = 'tutorial'
urlpatterns = [
  # The home view ('/tutorial/')
  url(r'^$', views.home, name='home'),
  # Explicit home ('/tutorial/home/')
  url(r'^home/$', views.home, name='home'),
  # Redirect to get token ('/tutorial/gettoken/')
  url(r'^gettoken/$', views.gettoken, name='gettoken'),
  # Mail view ('/tutorial/mail/')
  url(r'^mail/$', views.mail, name='mail'),
  # Events view ('/tutorial/events/')
  url(r'^events/$', views.events, name='events'),
  # Contacts view ('/tutorial/contacts/')
  url(r'^contacts/$', views.contacts, name='contacts'),
]