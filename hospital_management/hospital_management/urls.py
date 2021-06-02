from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('accounts/', include('authentication.urls')),
    
    path('panel/', include('panel.urls')),
]
