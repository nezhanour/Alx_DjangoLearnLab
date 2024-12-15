from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'token']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio',''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        token = Token.objects.create(user=user)  # Create token here
        user.token = token.key  # Attach token to the user object for response
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)  # Ensure token is created or retrieved
            return {'username': user.username, 'token': token.key}
        raise serializers.ValidationError("Incorrect credentials")