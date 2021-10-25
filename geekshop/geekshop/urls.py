from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('shop/', include('mainapp.urls')),
    path('admin/', admin.site.urls,),
    path('', mainapp.main, name='main'),
    path('test/', mainapp.temp, name='temp'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    # path('products/', include('mainapp.urls', namespace='products'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)