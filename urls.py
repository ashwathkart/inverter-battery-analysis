from django.urls import path
from . import views
from . import theapp

urlpatterns = [
    path('', theapp.battery, name = 'battery'),
    # path('test/', views.test[3], name = 'test')
]