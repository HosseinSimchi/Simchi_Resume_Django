from django.urls import path
from Resume.views import index_view

urlpatterns = [
    path('', index_view, name = "index"),
]

