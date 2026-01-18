from rest_framework import serializers
from .models import User, UserProfile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password','role']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, data):
        user = User.objects.create_user(**data)
        UserProfile.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
