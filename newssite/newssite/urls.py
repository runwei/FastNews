from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from blog import views

urlpatterns = patterns('',
   # url(r'^$', views.index, name='index'),
    url(r'^$', views.index,name='index'),
    url(r'^index.html$', views.index,name='index'),
    # url(r'^login/$', 'accounts.views.login_user', name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    # url(r'^galleries.html$', views.galleries,name='galleries'),
    # url(r'^contact.html$', views.contact,name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #         {'document_root': settings.STATIC_ROOT}),
)
