from django.conf.urls import url,include,patterns
from retrospective import views

# urlpatterns = [
# 	url(r'^$',views.index),
# ]

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index), # ADD THIS NEW TUPLE!
)