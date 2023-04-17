from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test),
    path('restricted/', views.restricted_view),
    path('stories', views.all_stories),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
