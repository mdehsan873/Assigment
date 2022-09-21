from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, Company, Team


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User

        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['uuid', 'name', 'ceo_name', 'address', 'inception_date']

    def create(self, validated_data):
        return Company.objects.create(**validated_data)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['uuid', 'lead_name', 'companyID']

    def create(self, validated_data):
        return Team.objects.create(**validated_data)
