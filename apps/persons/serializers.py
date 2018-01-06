from rest_framework import serializers
from apps.persons.models import User,StoreAdmin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName','password','nickname','remainder')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreAdmin
        fields = ('adminId','adminPassword','adminEmail')
