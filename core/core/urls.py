"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('payment/', include('payment.urls')),
    path('review/', include('review.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.SHOW_DEBUGGER_TOOLBAR:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')),]



handler400 = "core.error_views.error_400"  # bad_request
handler403 = "core.error_views.error_403"  # permission_denied
handler404 = "core.error_views.error_404"  # page_not_found
handler500 = "core.error_views.error_500"  # server_error