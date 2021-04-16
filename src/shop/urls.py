from django.urls import path

from shop.views import ShopListCreateView

app_name = 'shop'

urlpatterns = [
    path('', ShopListCreateView.as_view(), name='shop=create-list-api'),
]
