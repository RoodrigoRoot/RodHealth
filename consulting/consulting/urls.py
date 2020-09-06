from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("cuenta/", include("accounts.urls")),
    path("citas/", include("appoiments.urls")),
    path('admin/', admin.site.urls),
]
