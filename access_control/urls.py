from django.urls import path
from . import views
urlpatterns = [
    path('logs/', views.AccessLogViewSet.as_view(), name='accesslog-list'),
    path('logs/<int:pk>/', views.AccessLogDetailViewSet.as_view(), name='accesslog-detail'),    
]
    