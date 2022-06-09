from django.db.models import fields
from rest_framework import serializers
from .models import UserInfo, UserPreference


class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'userId',
            'userPreferenceEat',
            'userPreferenceDrink',
            'userPreferenceCafe'
        )
        model = UserPreference


class UserInfoSerializer(serializers.ModelSerializer):
    preference = UserPreferenceSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'userName',
            'userEmail',
            'userId',
            'userPassword',
            'userSex',
            'userAge',
            'userImage',
            'preference'
        )
        model = UserInfo


# class UserInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInfo
#         fields = ['userName', 'userEmail', 'userId', 'userPassword', 'userSex', 'userAge', 'userImage']