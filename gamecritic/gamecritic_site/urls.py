from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login_user/", views.login_user, name="login_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("games/", views.game_list, name="game_list"),
]