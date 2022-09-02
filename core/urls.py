"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from accounts.views.signup_in import SignIn, SignUp

schemaview = get_schema_view(
    title="Drone E-Shop",
    description="Api for e-commerce next app",
    version="1.0.0",
    urlconf="core.urls",
)

urlpatterns = [
    path('aaa', SignUp.as_view()),
    path('bbb', SignIn.as_view()),
    path('admin/', admin.site.urls),
    re_path(r'api/auth/', include('knox.urls')),
    path('schema/', schemaview)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
