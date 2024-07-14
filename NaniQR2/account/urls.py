from django.urls import path
from . import views
from django.contrib.auth.views import (

    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)



urlpatterns = [
    # Create a new urls.py file in the users app
    path('about-as/', views.about_us, name='about-us'),
    path('login_C/', views.Login_C, name='login_C'),
    path('register_C/', views.Register_C, name='register_C'),

    path('accounts/signup/agent/', views.AgentSignUpView.as_view(), name='agent_signup'),
    path('accounts/signup/store/', views.StoreSignUpView.as_view(), name='store_signup'),
    path('accounts/signup/admin/', views.AdminaSignUpView.as_view(), name='admin_signup'),
    
    path('agent_login/', views.AgentLoginView.as_view(redirect_authenticated_user=True),name='agent_login'),
    path('store_login/', views.StoreLoginView.as_view(redirect_authenticated_user=True),name='store_login'),
    path('admin_login/', views.AdminaLoginView.as_view(redirect_authenticated_user=True),name='admin_login'),

    path('agent_profile/', views.Agentpage, name='agent_profile'),
    path('store_profile/', views.Storepage, name='store_profile'),
    path('admin_profile/', views.Adminapage, name='admin_profile'),    

    path('logout/', views.LogoutView,name='logout'),
    path('password-reset/', 
        PasswordResetView.as_view(
            template_name='password_reset.html',
            html_email_template_name='password_reset_email.html'
        ),
        name='password-reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('download_img', views.download_img, name='download_img'),
    
]



