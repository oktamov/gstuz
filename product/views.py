from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer


class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('news', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        product_id = self.request.query_params.get('id', None)
        news = self.request.query_params.get('news', None)

        if product_id:
            queryset = Product.objects.get(id=product_id)
            if not queryset.exists():
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

            serializer = ProductDetailSerializer(queryset)
        elif news:
            queryset = Product.objects.order_by('-created_at')[:2]
            serializer = ProductSerializer(queryset, many=True)
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)
