from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    # path('create_link/', views.link_create, name='link_create'),
    path('create_card/', views.card_create, name='card_create'),
    # path('create_dp/', views.dp_create, name='dp_create'),
    # path('get_link/<str:pk>/', views.link_get, name='link_get'),
    path('get_card/<str:pk>/', views.card_get, name='card-get'),
    # path('get_dp/<str:pk>/', views.dp_get, name='dp-get'),
    path('test_case/', views.main_external_api, name='test_case')
]