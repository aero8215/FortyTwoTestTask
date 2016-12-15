from django.conf.urls import patterns, include, url, handler400, handler500
from django.contrib import admin
admin.autodiscover()

handler400 = 'apps.hello.views.page_not_found'
handler500 = 'apps.hello.views.bad_request'

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.hello.urls'))
)
