from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('addgamecritpost/', views.AddGamecritPost.as_view(), name='add_gamecrit_post'),
    path('<slug:slug>/', views.display_game_review, name='display_game_review'),
    path('<slug:slug>/comment_edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]