from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("username", " email", "password")
            extra_kwargs = {'password':{'write only' : True}}
        def create(self, validated_data):
              user = self.Meta.model.objects.create_user(**validated_data)
              return user
class LoginSerializer(serializers.Serializer):
      username = serializers.CharField()
      password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    