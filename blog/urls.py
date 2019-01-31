from . import views
from django.urls import path


urlpatterns = [
    path(r'ht', views.post_list, name='post_list'),
]