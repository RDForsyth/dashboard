from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='job_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^api/get_jobs/', views.get_jobs, name='get_jobs'),
#    url(r'^search/$', views.search, name='search'),
    url(r'^api/get_chart/', views.get_chart, name='get_chart'),
    url(r'^add_job', views.add_job, name='add_job'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.job_edit, name='job_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.job_remove, name='job_remove'),

]
