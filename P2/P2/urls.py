from  django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # pagina principal
    path('addon1/', include('addon1.urls')),
    path('addon2/', include('addon2.urls')),
]
