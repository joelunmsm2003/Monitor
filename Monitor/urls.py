from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
 	url(r'^logeate/', 'MonitorApp.views.logeate', name='reporte'),
 	url(r'^logeate/', 'MonitorApp.views.logeate', name='reporte'),
	url(r'^push$', 'MonitorApp.views.push'),
	url(r'^ticket/', 'MonitorApp.views.ticket'),
	url(r'^salir/', 'MonitorApp.views.salir'),
	url(r'^editar_ticket/(\d+)/$','MonitorApp.views.editar_ticket'),

	url(r'^atender/(\d+)/$','MonitorApp.views.atender'),
)
