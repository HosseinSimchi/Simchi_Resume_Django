from django.urls import path
from Resume.views import index_view,portfolio_view
app_name = "Hossein"
urlpatterns = [
    path('', index_view, name = "index"),
    path('About', portfolio_view, name = 'about')
]

