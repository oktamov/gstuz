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
            openapi.Parameter('product_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('category_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('product_last_count', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        product_id = self.request.query_params.get('product_id', None)
        category_id = self.request.query_params.get('category_id', None)
        product_last_count = self.request.query_params.get('product_last_count', None)
        if len(self.request.query_params) > 1:
            return Response({'error': 'You can only provide one query param'}, status=status.HTTP_400_BAD_REQUEST)

        elif product_id:
            try:
                queryset = Product.objects.get(id=product_id)
                serializer = ProductDetailSerializer(queryset)
            except Product.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        elif category_id:
            try:
                queryset = Product.objects.filter(category_id=category_id)
                serializer = ProductSerializer(queryset, many=True)
            except Product.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        elif product_last_count:
            product_last_count = int(product_last_count)
            print(product_last_count)
            queryset = Product.objects.order_by('-created_at')[:product_last_count]
            serializer = ProductSerializer(queryset, many=True)

        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)
