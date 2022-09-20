from rest_framework import serializers

from droneservice.models.service import Service, ServiceDetailValue, ServiceImage
from droneservice.models.order import orderedService
from droneservice.models.category import Category

from droneservice.models.category import Category


class ServiceImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceImage
        fields = ["image"]

class ServiceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceDetailValue
        fields = ['detail_key','value_key']
        depth = 1

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = orderedService
        fields = ['uuid', 'service','address']
        depth = 1

class ServiceSerializer(serializers.ModelSerializer):

    service_image = ServiceImageSerializer(read_only=True, many=True)
    service_detail = ServiceDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Service
        fields = ['uuid','owner','uuid','name','title','desc','price','category','service_detail','service_image']


    def create(self, data):

        print(self.context.get('service_images'))
        images = []
        for image in self.context.get('service_images'):
            images.append({'image': image})
        p_i_s = ServiceImageSerializer(data=images, many=True)

        if p_i_s.is_valid(raise_exception=True):
            try:
                category = Category.objects.get(uuid=data.get('category'))
                print(category.uuid)
                data.pop('category')
                data.pop('owner')
            except:
                raise serializers.ValidationError('something went wrong')

            service = self.Meta.model.objects.create(owner=self.context.get('request').user.user_profile, category=category, **data)

            for key, value in self.context.get('details').items():
                ServiceDetailValue.objects.create(service=service, detail_key = key, value_key = value)

            for image in images:
                ServiceImage.objects.create(service=service, image=image.get('image'))
        return data



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["uuid", "name"]
