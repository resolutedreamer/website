from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'hello.views.customer_new', name = 'sub_new'),
    url(r'^success.html', 'hello.views.success', name = 'success'),
    url(r'^login/$', 'hello.views.login', name = 'login'),
    #url(r'^logout/$', hello.views.logout, {'next_page': '/login/'}),

    #TO DELETE
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
]
