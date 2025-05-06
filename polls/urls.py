from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
]