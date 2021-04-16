from django.contrib.gis.measure import Distance
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import status

from shop.models import Shop
from shop.serializer import ShopSerializer
from user.permissions import IsSuperUser
from user.serializers import UserLiteSerializer


class ShopListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsSuperUser)
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter()

    def get_queryset(self):
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        if not self.request.query_params.get('lat') or not self.request.query_params.get('lon'):
            raise ValidationError(detail='invalid request', code=status.HTTP_400_BAD_REQUEST)
        queryset = self.queryset
        if self.request.query_params.get('name'):
            queryset = queryset.filter(name__istartswith=self.request.query_params['name'])
        if self.request.query_params.get('is_active'):
            queryset = queryset.filter(is_active=True)
        queryset = queryset.filter(
            location__distance_lt=(
                f'Point({lat} {lon})',
                Distance(km=.2)
            )
        )
        return queryset

    def create(self, request, *args, **kwargs):
        self.request.data['location'] = f'Point({self.request.data["lat"]} {self.request.data["lon"]})'
        return super(ShopListCreateView, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        created_by = UserLiteSerializer(self.request.user).data
        serializer.save(created_by=created_by)
