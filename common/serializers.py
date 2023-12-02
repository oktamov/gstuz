from rest_framework import serializers

from utils.regex import phone_regex
from .models import Category, Document, Form, Address, Company, Region, District


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'type']


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'full_name', 'organization', 'phone_number', 'email', 'desc']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']


class AddressSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    region = RegionSerializer(source='district.region', read_only=True)

    class Meta:
        model = Address
        fields = ['id', 'address1', 'address2', 'lat', 'lng', 'postal_code', 'metro', 'district', 'region']


class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'phone1', 'phone2', 'email', 'web_site', 'address']


class SendVerificationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[phone_regex])
