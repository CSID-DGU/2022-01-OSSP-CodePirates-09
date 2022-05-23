from django.db.models import fields
from rest_framework import serializers
from .models import UserInfo, UserPreference, UserPartner


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'userName',
            'userEmail',
            'userId',
            'userPassword',
            'userSex',
            'userAge',
            'userImage'
        )
        model = UserInfo


# class UserInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInfo
#         fields = ['userName', 'userEmail', 'userId', 'userPassword', 'userSex', 'userAge', 'userImage']

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'userId',
            'preferenceEat',
            'preferencePlay',
            'preferenceDrink',
            'preferenceSee',
            'preferenceWalk'
        )
        model = UserPreference


class UserPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'userPartnerName',
            'userPartnerDate',
            'userPartnerImage'
        )
        model = UserPartner
