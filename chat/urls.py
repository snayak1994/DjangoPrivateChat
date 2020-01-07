from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register
urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout', )

]
