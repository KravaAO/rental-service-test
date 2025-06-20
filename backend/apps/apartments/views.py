from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
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
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    filterset_fields = {
        'availability': ['exact'],
        'number_of_rooms': ['exact'],
        'price': ['gte', 'lte'],
    }
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'number_of_rooms', 'created_at']
    ordering = ['-created_at']
    #search_fields = ['name', 'description']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]

    def get_serializer_class(self):
        if self.action == 'list':
            return ApartmentListSerializer
        if self.action == 'retrieve':
            return ApartmentDetailSerializer
        return ApartmentCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
