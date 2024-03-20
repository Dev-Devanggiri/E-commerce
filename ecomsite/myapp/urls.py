from django.urls import path
from . import views
from myapp import views as myapp_views
from django.contrib.auth import views as auth_views

app_name = 'myapp'

urlpatterns = [
    # path('', views.index, name='home'),
    # path('login/', views.MyLoginView.as_view(), name='login'),
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    path("login/",auth_views.LoginView.as_view(template_name='myapp/login.html'), name="login"),
    path("signup/",myapp_views.user_signup, name="signup"),
    path("logout/",auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name="logout"),
    # path('logout/', views.user_logout, name='logout'),
]