from django.conf.urls import patterns, include, url
from django.contrib import admin
from retrospective import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index), # ADD THIS NEW TUPLE!
    url(r'^memberForm$',views.memberForm),
    url(r'^loginUser/$',views.loginUser),
    url(r'^manager_set_up_form/$',views.manager_set_up_form),
    url(r'^meeting/$',views.meeting),
    url(r'^addQuestion/$',views.addQuestion),
)
