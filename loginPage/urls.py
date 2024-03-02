from django.contrib import admin
from django.urls import path, include
from loginApp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("loginApp.urls")),
]
