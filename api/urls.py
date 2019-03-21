from extensionworkers import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings

from django.urls import include, path, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('extensionworkers.urls')),
    url(r'^accounts/signup/$', views.signup, name='signup'),
    url(r'^accounts/login/$',
        auth_views.LoginView.as_view(
            template_name="registration/login.html"),
        name="login"),
    url(r'^accounts/logout/$', views.url_redirect, name="url-redirect"),
]
