from django.urls import path, include
from django.conf.urls import url

#from Order import views
from PersonInfo import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'rest_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^order/', views.order_List,name='order_list'),
    #url(r'^order/(?P<pk>[0-9]+)/$', views.order_detail,name='order_detail'),
    url(r'^personinfo/(?P<pk>[0-9]+)/$', views.personinfo_detail,name='personinfo_detail'),
]