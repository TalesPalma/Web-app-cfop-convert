from django.urls import path
from app_cfop import views
urlpatterns = [
    path('',views.home,name="home"),
    path('listarDados/',views.listarDados,name="listarDados"),
]

