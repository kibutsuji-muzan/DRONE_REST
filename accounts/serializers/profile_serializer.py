from accounts.models.userModel import User
from accounts.models.profileModel import UserProfile, ProfileImage

from rest_framework import serializers

from phonenumbers import parse as validate_phone
from pyisemail import is_email as validate_email

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', ]


class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileImage
        fields = ['image']

    def update(self, instance, data):
        instance.image = data.get('image')
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):

    profile_image = ProfileImageSerializer()

    class Meta:
        model = UserProfile
        fields = ['email', 'phone', 'first_name', 'last_name', 'gender', 'birthday', 'profile_image']

    def validate(self, data):
        if data.get('email'):
            email = validate_email(address= data.get('email'), check_dns=True, diagnose=True)
            if email:
                pass
        if data.get('phone'):
            phone = validate_phone(data.get('phone'),None)
            if phone:
                pass
        if data.get('profile_image'):
            pass
        return data
        
    def update(self, instance, data):
        instance.first_name = data.get('first_name')
        instance.last_name = data.get('last_name')
        instance.email = data.get('email')
        instance.gender = data.get('gender')
        instance.birthday = data.get('birthday')

        p_s = ProfileImageSerializer(data=data.get('profile_image'))
        if p_s.is_valid(raise_exception=True):
            p_s.update(instance=instance.profile_image, data=data.get('profile_image'))
            instance.save()
        return instance