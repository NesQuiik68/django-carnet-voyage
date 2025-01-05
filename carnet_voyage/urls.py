from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/voyages/')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('voyages/', include('voyages.urls')),
]