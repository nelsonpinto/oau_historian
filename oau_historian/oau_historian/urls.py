from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from django.contrib.auth.views import login
#from django.contrib.auth.views import logout

urlpatterns = patterns('',    
    url(r'^$', 'hist.views.home'),
    url(r'^hist/$', 'hist.views.index'),
    
    url(r'^user/createaccount/$', 'hist.views.user_createaccount'),
    url(r'^user/signin/$', 'hist.views.user_signin'),
    url(r'^user/signout/$', 'hist.views.user_signout'),
    url(r'^user/private/$', 'hist.views.user_private'),

    url(r'^hist/controller/$', 'hist.views.controller_index'),

    url(r'^hist/snapshot/$', 'hist.views.snapshot_index'),

    url(r'^hist/snapshot/(\d+)/$', 'hist.views.trend_index'),     
    url(r'^hist/trend/add/(\d+)/$', 'hist.views.trend_add'),
    url(r'^hist/trend/edit/(\d+)/$', 'hist.views.trend_edt'),
    url(r'^hist/trend/remove/(\d+)/$', 'hist.views.trend_rem'),

    url(r'^hist/connect/$', 'hist.views.connect_index'),
    url(r'^hist/connect/add/$', 'hist.views.connect_add'),
    url(r'^hist/connect/edit/(\d+)/$', 'hist.views.connect_edt'),
    url(r'^hist/connect/remove/(\d+)/$', 'hist.views.connect_rem'),

    url(r'^hist/tag/$', 'hist.views.tag_index'),
    url(r'^hist/tag/add/$', 'hist.views.tag_add'),
    url(r'^hist/tag/edit/(\d+)/$', 'hist.views.tag_edt'),
    url(r'^hist/tag/remove/(\d+)/$', 'hist.views.tag_rem'),

    url(r'^hist/objects/$', 'hist.views.ObjectoNoExiste'),

    url(r'^report/$', 'report.views.report_index'),
    url(r'^report/generar/(\d+)/$', 'report.views.report_generar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
