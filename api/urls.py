from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('test/', views.test),
    path('restricted/', views.restricted_view),
    path('stories/', views.all_stories),
    path('stories/create/', views.create_story),
    path('stories/user/', views.user_stories),
    path('stories/<int:id>/', views.all_stories),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
