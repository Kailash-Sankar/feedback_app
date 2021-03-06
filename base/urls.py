from django.conf.urls import url
from . import views

urlpatterns = [
    #Home
    url(r'^$', views.home, name='home'),

    #Auth
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    #meta debug
    url(r'^meta/$', views.display_meta, name='meta'),

    #category
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^cat/([0-9]+)$', views.category, name='category'),
    url(r'^cat/([0-9]+)/questions/([0-9]*)$', views.questions, name='questions'),

    #save
    url(r'^cat/([0-9]+)/save$', views.saveForm, name='saveForm'),
    url(r'^cat/([0-9]+)/answers/save$', views.saveAnswers, name='saveAnswers'),

    #views
    url(r'^feed/([0-9]+)/view$', views.viewFeedback, name='viewFeedback'),
    url(r'^activity$', views.activity, name='activity'),

    #profile
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^me/$', views.me, name='me'),

    #vendors
    url(r'^cat/([0-9]+)/loc/([0-9]+)/vendors$', views.vendors, name='vendors'),

    #support
    url(r'^help$', views.help, name='help'),

    #reports
    url(r'^report$', views.report, name='report'),
    url(r'^report/cat/([0-9]+)$', views.report_cat, name='report_cat'),

]
