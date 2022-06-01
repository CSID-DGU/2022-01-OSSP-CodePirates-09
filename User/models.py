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
    preferenceEat = models.TextField(blank=True)
    preferencePlay = models.TextField(blank=True)
    preferenceDrink = models.TextField(blank=True)
    preferenceSee = models.TextField(blank=True)
    preferenceWalk = models.TextField(blank=True)


class UserPartner(models.Model):
    id = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='userId')
    userPartnerName = models.TextField(blank=True)
    userPartnerDate = models.IntegerField(blank=True)
    userPartnerImage = models.TextField(blank=True)
