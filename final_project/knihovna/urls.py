from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_users/', views.list_users, name='list_users'),
    path('user/<int:id>', views.user, name='user'),
    path('game/<int:id>', views.game, name='game'),
    path('list_games/', views.list_games, name='list_games'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)