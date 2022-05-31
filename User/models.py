from django.db import models


# class UserInfo(models.Model):
#     userName = models.TextField()
#     userEmail = models.TextField()
#     userId = models.TextField(primary_key=True)
#     userPassword = models.TextField()
#     userSex = models.TextField()
#     userAge = models.TextField()
#     userImage = models.TextField(blank=True, default='')


class UserPreference(models.Model):
    id = models.BigAutoField(primary_key=True)
    # userId = models.TextField(primary_key=True)
    preferenceEat = models.TextField(blank=True)
    preferencePlay = models.TextField(blank=True)
    preferenceDrink = models.TextField(blank=True)
    preferenceSee = models.TextField(blank=True)
    preferenceWalk = models.TextField(blank=True)


class UserPartner(models.Model):
    id = models.BigAutoField(primary_key=True)
    # userId = models.TextField(primary_key=True)
    userPartnerName = models.TextField(blank=True, default="")
    userPartnerDate = models.IntegerField(blank=True, null=True)
    userPartnerImage = models.TextField(blank=True, default="")


class UserInfo(models.Model):
    userName = models.TextField()
    userEmail = models.TextField()
    userId = models.TextField(primary_key=True)
    userPassword = models.TextField()
    userSex = models.TextField()
    userAge = models.TextField()
    userImage = models.TextField(blank=True, default='')
    preference = models.OneToOneField(UserPreference, on_delete=models.CASCADE, db_column='preference', null=True, blank=True)
    partner = models.OneToOneField(UserPartner, on_delete=models.CASCADE, db_column='partner', null=True, blank=True)
