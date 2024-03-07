from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from store.models import Product


@api_view(['GET'])
def get_data(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def post_data(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer)


@api_view(['POST'])
def update_order_item(request):
    customer = request.user


