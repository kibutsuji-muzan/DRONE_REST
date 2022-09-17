from rest_framework.serializers import ModelSerializer

from droneshop.models.product import Product, ProductDetailValue, ProductImage, ProductVerificationRequest
from droneshop.models.orders import orderedItem

class ProductImageSerializer(ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ["image", "alt_text"]

class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = ProductDetailValue
        fields = ['detail_key','value_key']
        depth = 1

class OrderSerializer(ModelSerializer):

    class Meta:
        model = orderedItem
        fields = ['orderId', 'product']
        depth = 1

class ProductSerializer(ModelSerializer):
    product_image = ProductImageSerializer(read_only=True, many=True)
    product_detail = ProductDetailSerializer(many=True)
    class Meta:
        model = Product
        fields = ['product_detail','product_image','owner','category','categoryByUser','uuid','name','title','desc','slug','price']



