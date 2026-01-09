from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate(self, attrs):
        username = attrs.get("username")
        email = attrs.get("email")
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if not username:
            raise serializers.ValidationError({"username": "Это поле обязательно."})
        if not email:
            raise serializers.ValidationError({"email": "Это поле обязательно."})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Такой username уже занят."})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Такой email уже зарегистрирован."})

        if password != password2:
            raise serializers.ValidationError({"password2": "Пароли не совпадают."})


        try:
            validate_password(password)
        except DjangoValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs.get("username"), password=attrs.get("password"))
        if not user:
            raise serializers.ValidationError({"detail": "Неверный логин или пароль."})
        if not user.is_active:
            raise serializers.ValidationError({"detail": "Пользователь не активен."})

        refresh = RefreshToken.for_user(user)
        return {
            "user": user,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
