from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404,handler500,handler403,handler400
from errors import views as error_views
# currently working
urlpatterns = [
      path('i18n/',include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('support/', include('support.urls')),
    # path('errors/', include('errors.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'errors.views.error_404'
handler500 = 'errors.views.error_500'
handler403 = 'errors.views.error_403'
handler400 = 'errors.views.error_400'