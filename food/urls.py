from django.urls import path
from . import views

urlpatterns = [
    path('chinese', views.chinese, name='chinese'),
    path('order', views.order, name='order'),
    path('success', views.success, name="success")
]
