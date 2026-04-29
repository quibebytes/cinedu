from django.urls import path
from app import views

app_name = 'cinedu'
urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.cadastro, name='cadastro'),
]
