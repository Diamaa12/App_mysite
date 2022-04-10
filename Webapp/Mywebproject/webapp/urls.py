from django.urls import path
from .views import  index_webapp
urlspatterns = [
    path('',index_webapp, name="web-app")
]