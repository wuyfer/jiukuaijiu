"""jiukuaijiu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('goods.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^user/', include('user.urls')),
]
from  jiukuaijiu import settings
if settings.DEBUG:
    from  django.views.static import serve
    urlpatterns.append(url(r'^media/(?P<path>.*)$',serve,kwargs={'document_root':settings.MEDIA_ROOT}))
# from django.contrib.staticfiles.urls import static
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
