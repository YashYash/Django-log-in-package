from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


)

urlpatterns = patterns('',
    # url(r'^signup$', 'auth_app.views.signup', name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^secret/$', 'auth_app.views.special_page', name='secret'),
    # url(r'^accounts/login$', 'auth_app.views.login1', name='login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', 'auth_app.views.index', name='index'),
          #override the default urls
      url(r'^accounts/password/change/$',
                    auth_views.password_change,
                    name='password_change'),
      url(r'^accounts/password/change/done/$',
                    auth_views.password_change_done,
                    name='password_change_done'),
      url(r'^accounts/password/reset/$',
                    auth_views.password_reset,
                    name='password_reset'),
      url(r'^accounts/password/reset/done/$',
                    auth_views.password_reset_done,
                    name='password_reset_done'),
      url(r'^accounts/password/reset/complete/$',
                    auth_views.password_reset_complete,
                    name='password_reset_complete'),
      url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                    auth_views.password_reset_confirm,
                    name='password_reset_confirm'),

      #and now add the registration urls
      url(r'', include('registration.backends.default.urls')),
)