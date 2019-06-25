from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('new/', new, name="new"),
    path('delete/<int:pk>', delete, name="delete"),
    path('update/<int:pk>', update, name="update")
]
