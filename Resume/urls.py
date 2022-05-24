from django.urls import path
from Resume.views import index_view,about_view,contact_view
app_name = "Hossein"
urlpatterns = [
    path('', index_view, name = "index"),
    path('About', about_view, name = 'about'),
    path('Contact', contact_view, name = 'contact')
]

