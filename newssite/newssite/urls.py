from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from blog import views
from django.conf.urls.static import static

urlpatterns = [ url(r'^$', views.index,name='index'),
    url(r'^index/$', views.index,name='index'),
    url(r'^world/$', views.world,name='world'),
    url(r'^entertainment/$', views.entertainment,name='entertainment'),
    url(r'^sport/$', views.sport,name='sport'),
    
    # url(r'^login/$', 'accounts.views.login_user', name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^chrome_archive/$', views.chrome_archive, name='chrome_archive'),
    url(r'^get_data/$', views.get_data, name='get_data'),
    url(r'^chrome_todaypick/$', views.chrome_todaypick, name='chrome_todaypick'),    
    url(r'^chrome_login/$', views.chrome_login, name='chrome_login'),
    url(r'^chrome_bookmark/$', views.chrome_bookmark, name='chrome_bookmark'),
    url(r'^login/$', views.login_user, name='login'),
    # url(r'^galleries.html$', views.galleries,name='galleries'),
    # url(r'^contact.html$', views.contact,name='contact'),
    url(r'^admin/', include(admin.site.urls))
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #         {'document_root': settings.STATIC_ROOT}),

