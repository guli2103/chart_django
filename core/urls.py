from django.urls import path
from .views import *


urlpatterns = [
    path('chart/', chart),
    path('example/',example),
]