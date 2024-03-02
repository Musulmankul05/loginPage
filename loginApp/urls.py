from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import IndexView, LoginPageView, RegisterView, SuccessView, logout

app_name = 'loginApp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/success&?/<uuid:uuid>/', SuccessView.as_view(), name='success'),
    path('logout/', logout, name='logout'),
]
