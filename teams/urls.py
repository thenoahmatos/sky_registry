from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('create/', views.team_create, name='team_create'),
    path('team/<int:team_id>/edit/', views.team_edit, name='team_edit'),
    path('team/<int:team_id>/delete/', views.team_delete, name='team_delete'),
]