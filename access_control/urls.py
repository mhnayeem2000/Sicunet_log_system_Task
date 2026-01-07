from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('api/logs/', views.AccessLogViewSet.as_view(), name='accesslog-list'),
    path('api/logs/<int:pk>/', views.AccessLogDetailViewSet.as_view(), name='accesslog-detail'),    
]
    