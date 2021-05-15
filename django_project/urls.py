"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

from users import api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', api_views.UserViewset)
router.register('post', api_views.PostViewset)
router.register('Profile', api_views.ProfileViewset)

urlpatterns = [

    path('restapi/', include(router.urls)),
    path ('restapi/', include('rest_framework.urls', namespace = 'restframework')),

    path('admin/', admin.site.urls),

    path('register/', user_views.register, name = 'register'),

    path('profile/', user_views.profile, name = 'profile'),

    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),

    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
   # path('login1/', user_views.login, name = 'login1'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name = 'password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name = 'password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name = 'password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name = 'password_reset_complete'),

    path('', include('blog.urls')),


    path ('home/',user_views.home_view, name = 'home_view'),
] 
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)