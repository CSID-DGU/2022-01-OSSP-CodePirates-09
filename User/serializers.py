from django.db.models import fields
from rest_framework import serializers
from .models import UserInfo, UserPreference, UserPartner


class UserPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'userId',
            'userPartnerName',
            'userPartnerDate',
            'userPartnerImage'
        )
        model = UserPartner


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


class UserInfoSerializer(serializers.ModelSerializer):
    partner = UserPartnerSerializer(many=True, read_only=True)
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
            'preference',
            'partner'
        )
        model = UserInfo


# class UserInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInfo
#         fields = ['userName', 'userEmail', 'userId', 'userPassword', 'userSex', 'userAge', 'userImage']