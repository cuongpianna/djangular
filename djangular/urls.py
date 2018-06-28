"""djangular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.views import obtain_jwt_token
from users import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('users.urls')),
    path('login',obtain_jwt_token, name='login'),
    path('register/',csrf_exempt(views.UserRegisterView.as_view())),
    path('',views.index,name='index'),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('api/',include('books.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,settings.STATICFILES_DIR)

