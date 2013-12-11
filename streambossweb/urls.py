from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

ACCEPTED_RESOURCE_PATTERN = "[-_.0-9A-Za-z ]"
VERSION = 'dev'

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^registerstream/', TemplateView.as_view(template_name='register_stream.html'), name='register_stream'),
    url(r'^registeroperation/', TemplateView.as_view(template_name='register_operation.html'), name='register_operation'),
    url(r'^createstream/', TemplateView.as_view(template_name='create_stream.html'), name='create_stream'),
    url(r'^streams/', TemplateView.as_view(template_name='streams.html'), name='streams'),
    url(r'^api/%s/streams/(%s+)$' % (VERSION, ACCEPTED_RESOURCE_PATTERN), 'streambossweb.web.api.stream_resource'),
    url(r'^api/%s/streams/?$' % VERSION, 'streambossweb.web.api.streams'),
    url(r'^api/%s/operations/(%s+)$' % (VERSION, ACCEPTED_RESOURCE_PATTERN),
        'streambossweb.web.api.operation_resource'),
    url(r'^api/%s/operations/?$' % VERSION, 'streambossweb.web.api.operations'),
)
