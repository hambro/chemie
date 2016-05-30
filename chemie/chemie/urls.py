"""chemie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views

import elections
urlpatterns = [
    url(r'^valg/', include('elections.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls'), name='frontpage'),
    url(r'^shitbox/', include('shitbox.urls')),
    url(r'^verv/', include('committiees.urls')),
    url(r'^bokskap/', include('lockers.urls'), name='bokskap'),
    url(r'^klassekatalog/', include('yearbook.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^calendar/', include('webcalendar.urls')),
    url(r'^profile/', include('customprofile.urls')),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout, {'next_page': '/'}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
