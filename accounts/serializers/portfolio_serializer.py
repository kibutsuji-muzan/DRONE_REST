from accounts.models.portfolio import Portfolio, PostImage, PortfolioPost

from rest_framework import serializers


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ['image', 'alt_txt']


class PortfolioPostserializer(serializers.ModelSerializer):

    post_image = PostImageSerializer(many=True, required=False)

    class Meta:
        model = PortfolioPost
        fields = ['caption', 'post_image']

    def validate(self, data):
        images = self.context.get('images')
        if images is not None:
            if len(images) > 6:
                raise serializers.ValidationError('More Than 4 Images Not Allowed In Posts')
        return data

    def create(self, validated_data):
        images = []
        for image in self.context.get('images'):
            images.append({'image': image})
        p_i_s = PostImageSerializer(data=images, many=True)
        if p_i_s.is_valid(raise_exception=True):
            post = self.Meta.model.objects.create(**validated_data)
            for image in images:
                PostImage.objects.create(image=image.get('image'), image_of=post)
            return validated_data
        raise serializers.ValidationError('images not valid')


class WithPostsSerializer(serializers.ModelSerializer):
    posts = PortfolioPostserializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = ['owner', 'title', 'bio', 'links', 'posts']


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['title', 'bio', 'links']

    def create(self, data):
        try:
            profile = self.context.get('request').user.user_profile
        except:
            raise serializers.ValidationError('Users Profile Not Exsist')
        self.Meta.model.objects.create(owner = profile, **data)

    def update(self, instance, data):
        try:
            profile = self.context.get('request').user.user_profile
        except:
            raise serializers.ValidationError('Users Profile Not Exsist')

        try:
            instance.bio = data.get('bio')
            instance.title = data.get('title')
            instance.links = data.get('links')
        except:
            pass
        instance.save()
        return data