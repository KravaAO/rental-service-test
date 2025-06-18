from rest_framework import serializers
from .models import Apartment


class ApartmentListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Apartment
        fields = [
            'name', 'slug', 'price', 'number_of_rooms',
            'square', 'availability', 'owner'
        ]


class ApartmentDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Apartment
        fields = '__all__'
        read_only_fields = ('slug', 'owner', 'created_at', 'updated_at')


class ApartmentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = [
            'name', 'description', 'price', 'number_of_rooms',
            'square', 'availability'
        ]
