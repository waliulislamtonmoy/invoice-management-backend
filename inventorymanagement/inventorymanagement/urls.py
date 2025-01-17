
from django.contrib import admin
from django.urls import path,include


from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("AppAccount.urls")),
    path("api/",include("Products.urls")),
    path("api/",include("Categories.urls")),
    path("api/",include("Customer.urls")),
    path("api/",include("Invoice.urls")),
    path("api/",include("Dashboard.urls")),
   
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)