# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-09T22:34:30+05:30
# @Email:  tamyworld@gmail.com
# @Filename: urls.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-10T13:15:27+05:30



from django.conf.urls import patterns, include, url

from django.contrib import admin
from core import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(urls)),
)
