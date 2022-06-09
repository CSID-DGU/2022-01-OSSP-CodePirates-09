from django.db import models


class UserInfo(models.Model):
    userName = models.TextField()
    userEmail = models.TextField()
    userId = models.TextField(primary_key=True)
    userPassword = models.TextField()
    userSex = models.TextField()
    userAge = models.TextField()
    userImage = models.TextField(blank=True, default='')


class UserPreference(models.Model):
    id = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='userId')
    userPreferenceEat = models.TextField(blank=True)
    userPreferenceDrink = models.TextField(blank=True)
    userPreferenceCafe = models.TextField(blank=True)
