from django.urls import path

from user.views import registration

app_name = 'user'

urlpatterns = [
    path('', registration)
]
