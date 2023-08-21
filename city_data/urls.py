"""
URL conf at project level.
"""

# Third Party Imports
from django.contrib import admin
from django.urls import (
    path,
    include
)
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{settings.API_VERSION}/', include('backend.urls')),
    path(f'backend-build/', include('backend_build.urls'))
]
