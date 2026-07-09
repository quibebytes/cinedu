from django.urls import path
from app import views
from .forms import LoginForm
from django.contrib.auth.views import LoginView

app_name = 'cinedu'
urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='cinedu/login.html',
        authentication_form=LoginForm,
        redirect_authenticated_user=True,
        next_page='cinedu:home',
    ), name='login'),
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('detalhes/<int:doc_id>/', views.detalhes, name='detalhes'),
    path('video/<int:doc_id>/', views.video, name='video'),
    path('logout', views.logout, name='logout'),
]
