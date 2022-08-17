from rest_framework.serializers import ModelSerializer
from drone_api.models.product import Product, ProductImage
from drone_api.models.category import Category

class ProductImageSerializer(ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ["image", "alt_text"]

class ProductSerializer(ModelSerializer):
    product_image = ProductImageSerializer(read_only = True, many = True)
    class Meta:
        model = Product
        fields = ["id", "category", "name", "title", "desc", "slug", "price", "product_image"]

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["name", "slug"]