from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register_attempt', views.register_attempt, name='register_attempt'),
    path('login_attempt', views.login_attempt, name='login_attempt'),
    path('logout_attempt', views.logout_attempt, name='logout_attempt')
]
