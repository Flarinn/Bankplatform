"""
URL configuration for account project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.templatetags import rest_framework
from rest_framework.urlpatterns import format_suffix_patterns

from account import views
from account.views import index, about

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  path('', index, name='home'),
                  path('about', about, name='about'),
                  path('admin/', admin.site.urls),
                  # path('bank/', include('rest_framework.urls')),
                  # path('platform/', include('rest_framework.urls')),
                  # path('agent/', include('rest_framework.urls')),
                  path('agent/create', views.create, name='create'),
                  path('agent/createbencompany', views.create_ben_companies, name='createbencompany'),
                  path('agent/createprincompany', views.create_princ_companies, name='createprinccompany'),
                  path('login/', views.sign_in, name='agentlogin'),

                  path('logout', views.logout_user, name = 'agentlogout'),
                  path('agent/', views.agent),
                  path('agent/profile/<username>', views.profile, name='profile'),
                  path('application', views.application_list, name = 'applicationlist'),
                  path('application/<int:application_id>', views.application_info, name = 'applicationinfo'),
                  path('application/person',views.person_info, name = 'personinfo')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
