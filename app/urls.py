from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('i/', views.ind, name='ind'),
    path('forum/', views.forumm, name='forumm'),
    path('discussion/', views.discussionn, name='discussionn'),
]
