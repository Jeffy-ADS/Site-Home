from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.signup_view, name='signup'),
    path('404-preview/', views.preview_404_view, name='preview_404'),
    path('500-preview/', views.preview_500_view, name='preview_500'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]