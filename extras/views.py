from rest_framework import viewsets, status, mixins, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from extras.models.contactUs import Complaints, ContactUs, Review, Reports,     Service, Product

from phonenumbers import parse as validate_phone
from pyisemail import is_email as validate_email


class ContactUsSerializer(serializers.ModelSerializer):
    email_or_phone = serializers.CharField()

    class Meta:
        model=ContactUs
        fields=['name', 'email_or_phone']

    def valid_email_phone(self, email_or_phone):
        if validate_email(address=email_or_phone, check_dns=True):
            return {'email': email_or_phone, 'phone': False}
        try:
            if validate_phone(email_or_phone):
                return {'phone': email_or_phone, 'email': False}
        except:
            raise serializers.ValidationError('Not Valid')

    def create(self, validated_data):
        try:
            validated_data.get('email_or_phone')
        except:
            raise serializers.ValidationError('email_or_phone Field Is Required')
        email_or_phone = self.valid_email_phone(validated_data.get('email_or_phone'))
        if email_or_phone.get('email'):
            ContactUs.objects.create(email=email_or_phone.get('email'),name = validated_data.get('name'))
        ContactUs.objects.create(email=email_or_phone.get('phone'),name = validated_data.get('name'))
        return validated_data



class HelpDesk(viewsets.GenericViewSet):

    http_method_names=['post']

    def create(self, request):
        serializer = ContactUsSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.data)
            return Response('We Will Contact You Soon! Thank You For Request')
        return Response('Data Not Valid')

    @action(methods=['post'], detail=True, url_name='complaint', url_path='complaint')
    def complaint(self, request, pk):
        try:
            title = request.data.get('title')
            desc = request.data.get('desc')
            service = Service.objects.get(uuid=id)
        except:
            raise serializers.ValidationError('All Requested Fields Are Required, Or Prefix Was Incorrect')

        Complaints.objects.create(titel=title, desc=desc, user=request.user.user_profile, service=service)
        return Response('Your Complaint Has Been Registerd')

    @action(methods=['post'], detail=False, url_name='review', url_path='review')
    def review(self, request):
        try:
            review = request.data.get('review')
        except:
            raise serializers.ValidationError('All Requested Fields Are Required')

        Review.objects.create(user=request.user.user_profile, review=review)
        return Response('Your Review Has Been Registerd')

    @action(methods=['post'], detail=True, url_name='report', url_path='report')
    def complaint(self, request, pk):
        try:
            title = request.data.get('title')
            desc = request.data.get('desc')
            product = Product.objects.get(uuid=id)
        except:
            raise serializers.ValidationError('All Requested Fields Are Required, Or Prefix Was Incorrect')

        Reports.objects.create(titel=title, desc=desc, user=request.user.user_profile, product=product)
        return Response('Your Complaint Has Been Registerd')

    