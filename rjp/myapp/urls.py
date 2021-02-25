
from django.urls import path
from .views import *

app_name = 'jp1'
urlpatterns = [
    path("index-2/", index_view_2),
    path("about-us/", about_view),
    path("", index_view),
]
