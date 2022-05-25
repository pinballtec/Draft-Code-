from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('create_link/', views.link_create, name='link_create'),
    path('create_card/', views.card_create, name='card_create'),
    path('create_dp/', views.dp_create, name='dp_create')
]