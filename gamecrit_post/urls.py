from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('addgamecritpost/', views.AddGamecritPost.as_view(), name='add_gamecrit_post'),
    path('<slug:slug>/', views.display_game_review, name='display_game_review'),
    path('delete/<slug:pk>/', views.DeleteGamecritPost.as_view(), name='delete_gamecrit_post'),
    path('edit/<slug:pk>/', views.EditGamecritPost.as_view(), name='edit_gamecrit_post'),
    path('<slug:slug>/comment_edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]