from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path("login_user/", views.login_user, name="login_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("games/", views.game_list, name="game_list"),
    path("game_review_list/<int:game_id>/", views.game_review_list, name="game_review_list"),
    path('add_game/', views.add_game, name='add_game'),
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
    path('add_review/<int:game_id>/', views.add_review, name='add_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


