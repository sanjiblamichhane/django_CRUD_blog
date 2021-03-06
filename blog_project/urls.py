"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include #importing path and include methods from django's built-in urls class


#order of the urls matter here
urlpatterns = [
    path('admin/', admin.site.urls), #admin entry
    path('accounts/', include('django.contrib.auth.urls')), #auth added
    path('accounts/', include('accounts.urls')), # new 
	path('', include('blog.urls')), #added by sl --> adding empty '' means that we're indicating that the URL requests should be redirected as to blog's URLs for further instructions. 
]
