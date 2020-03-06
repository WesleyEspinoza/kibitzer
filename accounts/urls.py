from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name="change-password"),
]
