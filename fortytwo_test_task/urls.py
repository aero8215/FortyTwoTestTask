from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.hello.urls')),
    url(
        regex=r'^static/(?P<path>.*)$',
        view='django.views.static.serve',
        kwargs={'document_root': settings.STATIC_ROOT, }
    )
)
