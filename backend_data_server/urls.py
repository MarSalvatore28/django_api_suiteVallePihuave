from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),  # Para la raíz
    path("homepage/", include("homepage.urls")),  # Para /homepage/
    path("demo/rest/api/", include("demo_rest_api.urls")),
]