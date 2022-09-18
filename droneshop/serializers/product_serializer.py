from rest_framework import serializers

from droneshop.models.product import Product, ProductDetailValue, ProductImage, ProductVerificationRequest
from droneshop.models.orders import orderedItem
from droneshop.models.category import Category

from droneshop.models.category import Category

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ["image"]

class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetailValue
        fields = ['detail_key','value_key']
        depth = 1

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = orderedItem
        fields = ['uuid', 'product']
        depth = 1

class ProductSerializer(serializers.ModelSerializer):

    product_image = ProductImageSerializer(read_only=True, many=True)
    product_detail = ProductDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['uuid','owner','uuid','name','title','desc','price','category','product_detail','product_image']



    def create(self, data):

        print(self.context.get('context').get('product_images'))
        images = []
        for image in self.context.get('context').get('product_images'):
            images.append({'image': image})
        p_i_s = ProductImageSerializer(data=images, many=True)

        if p_i_s.is_valid(raise_exception=True):
            try:
                category = Category.objects.get(uuid=data.get('category'))
                print(category.uuid)
                data.pop('category')
                data.pop('owner')
            except:
                raise serializers.ValidationError('something went wrong')

            product = self.Meta.model.objects.create(owner=self.context.get('request').user.user_profile, category=category, **data)

            for key, value in self.context.get('context').get('details').items():
                ProductDetailValue.objects.create(product=product, detail_key = key, value_key = value)

            for image in self.context.get('context').get('product_images'):
                ProductImage.objects.create(product=product, image=image)
        return data


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["uuid", "name"]
