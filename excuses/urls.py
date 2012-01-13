from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from excuses.core.views import Home


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
)

