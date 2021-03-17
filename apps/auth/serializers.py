from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,
                                     style={"input_type":   "password"})

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise serializers.ValidationError(
                {"email": "Provided e-mail address already exists."})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
