from django.urls import path
from basic_app.views import other,relative_url_templates,user_data

app_name = 'basic_app'
urlpatterns = [
    path('other/',other,name = 'other'),
    path('relative/',relative_url_templates,name = 'relative'),
    path('user_data/',user_data,name = 'userdata'),
]
