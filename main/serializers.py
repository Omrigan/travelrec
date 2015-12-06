from rest_framework import serializers
from main.models import TUsers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUsers