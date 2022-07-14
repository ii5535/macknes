from tokenize import Name
from django.urls import path,include
from page import views

urlpatterns = [
    path('',views.home,name='home'),
    path('translate/',views.translate,name='translate'),
    path('weather/',views.weather,name='weather'),
    path('notice/',views.notice,name='notice'),
    path('starplace/',views.starplace,name='starplace'),
]
