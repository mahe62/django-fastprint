"""
URL configuration for testProgrammer project.

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
from django.urls import path
from restAPI import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('restAPI.urls'))
# ]

urlpatterns = [
    path('list', views.produk_list, name='produk_list'),
    path('admin/', admin.site.urls),
    path('<int:id>/', views.produk_detail, name='produk_detail'),
    path('create/', views.produk_create, name='produk_create'),
    path('<int:id>/update/', views.produk_update, name='produk_update'),
    path('<int:id>/delete/', views.produk_delete, name='produk_delete'),
    path('', views.postapiproduk, name='api_data'),
    # path('post/', views.postapiproduk, name='post_data')



]