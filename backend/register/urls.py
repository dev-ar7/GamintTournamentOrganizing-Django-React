from django.urls import path
from .views import profile, login_view, register_view


urlpatterns = [
    path('profile', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('signup/', register_view, name='signup'),
]