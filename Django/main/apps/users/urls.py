from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
  url(r'^register$', views.register), 
  url(r'^login$', views.login), 
  url(r'^$', views.index), 
  url(r'^new$', views.new_user)
]