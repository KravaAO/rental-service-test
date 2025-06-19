from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from .filters import ApartmentFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as drf_filters
from .models import Apartment
from .serializers import (
    ApartmentListSerializer,
    ApartmentDetailSerializer,
    ApartmentCreateUpdateSerializer
)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Дозволено лише читання або якщо користувач є власником
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user




class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all().order_by('-created_at')
    serializer_class = ApartmentSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = ApartmentFilter
