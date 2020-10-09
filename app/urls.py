from django.urls import path
from . import views
from django.conf.urls.static import static
from among import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('i/', views.ind, name='ind'),
    path('forum/', views.forumm, name='forumm'),
    path('discussion/', views.discussionn, name='discussionn'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)