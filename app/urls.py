from django.urls import path
from . import views
from django.conf.urls.static import static
from among import settings

urlpatterns = [
    path('i/', views.home, name='home'),
    path('', views.ind, name='ind'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dcontact/', views.dcontact, name='dcontact'),
    path('work-with-us/', views.collaborate, name='collaborate'),
    path('faq/', views.faq, name='faq'),
    path('donate/', views.donate, name='donate'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('servers/', views.servers, name='servers'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('affiliate/', views.affiliate, name='affiliate'),
    path('general/', views.forumm, name='forumm'),
    path('discussion/', views.discussionn, name='discussionn'),
    path('general/<int:pk>', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)