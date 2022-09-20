from accounts.models.userModel import User, UpdateRequest, OrganizationType
from accounts.models.profileModel import UserProfile, ProfileImage

from rest_framework import serializers

from phonenumbers import parse as validate_phone
from pyisemail import is_email as validate_email

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','email', 'phone', 'email_verified', 'phone_verified']


class OrganizationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationType
        fields = ['type']



class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileImage
        fields = ['image']

    def update(self, instance, data):
        instance.image = data.get('image')
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):

    profile_image = ProfileImageSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'gender', 'birthday', 'profile_image']

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
        instance.user_profile.first_name = data.get('first_name')
        instance.user_profile.last_name = data.get('last_name')
        instance.user_profile.email = data.get('email')#remove it
        instance.user_profile.gender = data.get('gender')
        instance.user_profile.birthday = data.get('birthday')

        p_s = ProfileImageSerializer(data=data.get('profile_image'))
        if p_s.is_valid(raise_exception=True):
            print(p_s.data)
            p_s.update(instance=instance.user_profile.profile_image, data=data.get('profile_image'))
            instance.user_profile.save()
        return instance

class RequestUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpdateRequest
        fields = ['desc', 'organization_name', 'phone', 'org']

    def create(self, data):
        user = self.context.get('request').user
        data.pop('org')
        data['user']=user
        data['org']=self.context.get('org')
        print(data)
        self.Meta.model.objects.create(**data)
        return data
