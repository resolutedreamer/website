from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'hello.views.customer_new', name = 'sub_new'),
    url(r'^login/$', 'hello.views.login', name = 'login'),
    url(r'^logout/$', hello.views.logout, name = 'logout'),
]
