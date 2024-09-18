from rest_framework import serializers
from user.models import CustomUser

class UserClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_role', 'shop_name', 'shop_address', 'image', 'age', 'phone_number')
