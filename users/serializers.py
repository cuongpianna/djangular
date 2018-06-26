from rest_framework import serializers

from .models import Profile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('email','username','password','password2')

    def validate_email(self,email):
        existing = User.objects.filter(email = email).first()
        if existing:
            raise serializers.ValidationError('Someone with that email address has already registered. Was it you?')
        return email

    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("please enter a password and confirm it")

        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def create(self, validated_data):
        user = User(
            email = validated_data.get('email'),
            username = validated_data.get('username')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

