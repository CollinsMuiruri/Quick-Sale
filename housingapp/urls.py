from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.welcome_page, name='welcome'),
    url(r'^details/', views.details, name='details'),
    url(r'^tinymce/',include('tinymce.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
