from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:game_id>/', views.game, name='game'),
    path('overview/', views.overview, name='overview'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]