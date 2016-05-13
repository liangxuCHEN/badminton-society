from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from society import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home_page, name='home_page'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^member$',  views.member_index, name='member_index'),
    url(r'^member_creat$',  views.add_one_member, name='add_one_member'),
    url(r'^member_activited$',  views.member_activited, name='member_activited'),
    url(r'^update_balance$',  views.update_balance, name='update_balance'),
    url(r'^member_detail/(?P<member_id>\d+)/$', views.member_detail, name='member_detail'),
    url(r'^login$', views.LoginView, name='login'),
    url(r'^logout$', views.LogoutView, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bill_table$',  views.bill_table_index, name='bill_table_index'),
    url(r'^bill_table_create$',  views.add_bill_table, name='add_bill_table'),
    url(r'^bill_table_detail/(?P<table_id>\d+)/$', views.bill_table_detail, name='bill_table_detail'),
    url(r'^edit_bill_table/(?P<table_id>\d+)/$', views.edit_bill_table, name='edit_bill_table'),
    url(r'^add_bill_by_scran/(?P<person_id>\d+)/$', views.add_bill_by_scran, name="add_bill_by_scran"),
    url(r'^add_personal_bill', views.add_personal_bill, name='add_personal_bill'),
    url(r'^delete_personal_bill/(?P<personal_bill_id>\d+)/(?P<table_id>\d+)/$',
        views.delete_personal_bill, name='delete_personal_bill'),
    url(r'^download_bill/(?P<table_id>\d+)/$', views.download_bill, name='download_bill'),
    url(r'^download_member/$', views.download_member, name='download_member'),
)

"""
url(r'^item$',  views.item_index, name='item_index'),
    url(r'^item_creat$',  views.add_one_item, name='add_one_item'),
    url(r'^multitem_creat$',  views.add_multitems, name='add_multitems'),
    url(r'^bill_table$',  views.bill_table_index, name='bill_table_index'),
    url(r'^bill_table_create$',  views.add_bill_table, name='add_bill_table'),
    url(r'^bill_table_detail/(?P<table_id>\d+)/$', views.bill_table_detail, name='bill_table_detail'),
    url(r'^edit_bill_table/(?P<table_id>\d+)/$', views.edit_bill_table, name='edit_bill_table'),
    url(r'^add_bill', views.add_bill, name='add_bill'),
    url(r'^delete_bill/(?P<bill_id>\d+)/(?P<table_id>\d+)/$', views.delete_bill, name='delete_bill'),
    url(r'^download_bill/(?P<table_id>\d+)/$', views.download_bill, name='download_bill'),
    url(r'^login$', views.LoginView, name='login'),
    url(r'^logout$', views.LogoutView, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
"""
