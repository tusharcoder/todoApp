# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-10T13:14:17+05:30
# @Email:  tamyworld@gmail.com
# @Filename: urls.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-10T13:14:51+05:30


from django.conf.urls import url
from .views import *

urlpatterns = [
url(r'^tasks/$',TaskList.as_view(),name="get_all_tasks"),
url(r'^tasks/(?P<pk>[0-9]+)/$',TaskDetail.as_view()),
]
