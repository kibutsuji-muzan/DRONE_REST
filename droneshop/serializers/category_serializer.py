from rest_framework.serializers import ModelSerializer

from droneshop.models.category import Category, CategoryByUser

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["uuid", "name"]
