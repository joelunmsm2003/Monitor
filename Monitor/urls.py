from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
 	url(r'^logeate/', 'MonitorApp.views.logeate', name='reporte'),

	url(r'^push$', 'MonitorApp.views.push'),
	url(r'^ticket/(\d+)/$', 'MonitorApp.views.ticket'),
	url(r'^salir/', 'MonitorApp.views.salir'),
	url(r'^cerrar/(\d+)/$', 'MonitorApp.views.cerrar'),
	url(r'^validar/(\d+)/$', 'MonitorApp.views.validar'),
	url(r'^editar_ticket/(\d+)/$','MonitorApp.views.editar_ticket'),
	url(r'^ticket_add/', 'MonitorApp.views.ticket_add'),
	url(r'^atender/(\d+)/$','MonitorApp.views.atender'),
	url(r'^reasignar/(\d+)/$','MonitorApp.views.reasignar'),
	url(r'^ver_ticket/(\d+)/$','MonitorApp.views.ver_ticket'),
)
