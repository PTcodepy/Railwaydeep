# myapp/urls.py
from django.urls import path
from .views import index, personal

urlpatterns = [
    path('', index, name='index'),
    path('personal/', personal, name='personal'),
]
