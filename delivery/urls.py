"""
URL configuration for delivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
... # Other imports are here
from rest_framework import routers
from items.views import ItemsViewSet
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# items router
items_router = routers.SimpleRouter()
items_router.register(
    r'items',
    ItemsViewSet,
    basename='items',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(items_router.urls)),
    # path('api/auth/', include('authentication.urls')),
    path('auth/', include('user.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),

]

# redirect the root URL of our site (i.e. localhost:8000) to the URL localhost:8000/catalog/.
urlpatterns += [
    path('', RedirectView.as_view(url='items/', permanent=True)),
]

# enable the serving of static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)