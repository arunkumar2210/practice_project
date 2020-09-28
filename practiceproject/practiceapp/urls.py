from django.urls import path, re_path
from . import views

app_name = 'practiceapp'

urlpatterns = [

    path('', views.post_list_view),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list_view, name='post_list_by_tag_name'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
            views.post_detail_view, name='post_detail'),
    re_path(r'^(?P<id>\d+)/share/$', views.mail_send_view),
]
