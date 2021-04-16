from rest_framework import serializers

from shop.models import Shop
from user.serializers import UserLiteSerializer


class ShopSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    owner_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'

    def get_latitude(self, obj: Shop):
        return obj.latitude()

    def get_longitude(self, obj: Shop):
        return obj.longitude()

    def get_owner_details(self, obj: Shop):
        return UserLiteSerializer(obj.owner).data
