# myproject/urls.py
from django.contrib import admin
from django.urls import include, path
from myapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('', index, name='default'),
]
