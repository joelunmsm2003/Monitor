from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
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

	url(r'^reasignar_add/', 'MonitorApp.views.reasignar_add'),
	url(r'^atender/(\d+)/$','MonitorApp.views.atender'),
	url(r'^evento_add/(\d+)/$','MonitorApp.views.evento_add'),
	url(r'^reasignar/(\d+)/(\d+)/$','MonitorApp.views.reasignar'),
	url(r'^ver_ticket/(\d+)/$','MonitorApp.views.ver_ticket'),
	url(r'^realtime_post$', 'MonitorApp.views.realtime_post'),
	url(r'^realtime_post_monitor$', 'MonitorApp.views.realtime_post_monitor'),
	url(r'^detalle_ticket/(\d+)/$','MonitorApp.views.detalle_ticket'),
	url(r'^evento/(\d+)/(\d+)/$', 'MonitorApp.views.evento'),
	url(r'^evento_add/', 'MonitorApp.views.evento_add'),
	url(r'^ver_evento/(\d+)/(\d+)/$', 'MonitorApp.views.ver_evento'),
	url(r'^realtime/$', 'MonitorApp.views.realtime'),

	url(r'^ver_usuario/(\d+)/$', 'MonitorApp.views.ver_usuario'),
	url(r'^notificaciones/$', 'MonitorApp.views.notificaciones'),
	url(r'^ver_evento_all/(\d+)/$', 'MonitorApp.views.ver_evento_all'),
	url(r'^agregar_ticket/$', 'MonitorApp.views.list', name='list'),
	url(r'^list1/$', 'MonitorApp.views.list1', name='list1'),
	url(r'^documentos/(\d+)/$', 'MonitorApp.views.documentos'),
)


