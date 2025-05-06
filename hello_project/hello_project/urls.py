from django.contrib import admin
from django.urls import path
from greeting.views import hello_view

urlpatterns = [
    path('', hello_view),  
    path('admin/', admin.site.urls),
]
