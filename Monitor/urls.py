from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
 	url(r'^logeate/', 'MonitorApp.views.logeate', name='reporte'),
 	url(r'^logeate/', 'MonitorApp.views.logeate', name='reporte'),
	url(r'^push$', 'MonitorApp.views.push'),
	
	url(r'^reportes/', 'MonitorApp.views.reportes', name='reporte'),
	url(r'^salir/', 'MonitorApp.views.salir'),


)
