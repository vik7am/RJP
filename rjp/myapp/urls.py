
from django.urls import path
from .views import *

app_name = 'jp1'
urlpatterns = [
    path("index-2/", index_view_2),
    path("index2/", index_2_view),
    path("index3/", index_3_view),
    path("index4/", index_4_view),
    path("about-us/", about_view),
    path("", index_view),
]
