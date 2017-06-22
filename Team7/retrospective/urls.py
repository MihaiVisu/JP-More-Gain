from django.conf.urls import patterns, include, url
from django.contrib import admin
from retrospective import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index), # ADD THIS NEW TUPLE!
    url(r'^login$',views.login),
)