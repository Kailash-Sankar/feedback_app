from django.conf.urls import url
from . import views

urlpatterns = [
    #Home
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    #Auth
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    #meta debug
    url(r'^meta/$', views.display_meta, name='meta'),

    #category
    url(r'^cat/([0-9]+)$', views.category, name='category'),

    #Views
    url(r'^cat/([0-9]+)/questions$', views.questions, name='questions'),

    #Q&A
    url(r'^q/([0-9]+)$', views.question, name='question'),
    url(r'^question/([0-9]+)/answers/([0-9]*)$', views.answers, name='answers'),

    #save
    url(r'^question/([0-9]+)/answer/save$', views.saveAnswer, name='savea'),

    #profile
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^me/$', views.me, name='me'),
]
