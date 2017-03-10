from django.conf.urls import url
from Compiler import views

urlpatterns = [
url(r'^compile/$', views.handle_request),
]