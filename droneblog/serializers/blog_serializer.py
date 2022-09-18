from droneblog.models.blogs import Blog, BlogImage

from rest_framework import serializers


class BlogImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogImage
        fields = ['image', 'alt_txt']


class Blogserializer(serializers.ModelSerializer):

    blog_image = BlogImageSerializer(many=True, required=False)
    
    class Meta:
        model = Blog
        fields = ['user', 'id', 'title', 'content', 'blog_image']

    def validate(self, data):
        images = self.context.get('context')
        if images is not None:
            if len(images) > 6:
                raise serializers.ValidationError('More Than 4 Images Not Allowed In Posts')
        return data

    def create(self, validated_data):
        images = []
        for image in self.context.get('context'):
            images.append({'image': image})
        p_i_s = BlogImageSerializer(data=images, many=True)
        if p_i_s.is_valid(raise_exception=True):
            blog = self.Meta.model.objects.create(**validated_data)
            for image in images:
                BlogImage.objects.create(image=image.get('image'), blog=blog)
            return validated_data
        raise serializers.ValidationError('images not valid')


# class WithPostsSerializer(serializers.ModelSerializer):
#     posts = PortfolioPostserializer(many=True, read_only=True)

#     class Meta:
#         model = Portfolio
#         fields = ['title', 'bio', 'links', 'posts']


# class PortfolioSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Portfolio
#         fields = ['title', 'bio', 'links']

#     def create(self, data):
#         try:
#             print(self.context)
#             profile = self.context.get('request').user.user_profile
#         except:
#             raise serializers.ValidationError('Users Profile Not Exsist')
#         self.Meta.model.objects.create(owner = profile, **data)

#     def update(self, instance, data):
#         try:
#             print(self.context)
#             profile = self.context.get('request').user.user_profile
#         except:
#             raise serializers.ValidationError('Users Profile Not Exsist')

#         try:
#             instance.bio = data.get('bio')
#             instance.title = data.get('title')
#             instance.links = data.get('links')
#         except:
#             pass
#         instance.save()
#         return data