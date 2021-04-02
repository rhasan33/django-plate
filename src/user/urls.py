from django.urls import path

from user.views import registration, GetUsers

app_name = 'user'

urlpatterns = [
    path('', registration),
    path('/list', GetUsers.as_view())
]
