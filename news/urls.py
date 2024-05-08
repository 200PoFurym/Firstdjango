"""
URL configuration for news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from newsworld.views import home_page, MyFormView, single_news, MyLoginFormView, logout_view, category_page, \
    add_product_to_cart, user_cart, add_like, user_likes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('register', MyFormView.as_view()),
    path('news/<int:id>', single_news),
    path('login', MyLoginFormView.as_view()),
    path('logout', logout_view),
    path('category/<int:id>', category_page),
    path('add_to_cart/<int:id>', add_product_to_cart),
    path('user_cart', user_cart),
    path('add_like/<int:id>', add_like),
    path('user_likes', user_likes, name='user_likes')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)