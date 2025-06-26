from django.urls import path
from . import views

urlpatterns = [
    path('', views.ipo_list, name='ipo_list'),
    path('ipo/<int:pk>/', views.ipo_detail, name='ipo_detail'),

    # ✅ API URLs
    path('api/ipo/', views.IPOListAPI.as_view(), name='ipo_api_list'),
    path('api/ipo/<int:pk>/', views.IPODetailAPI.as_view(), name='ipo_api_detail'),
]
