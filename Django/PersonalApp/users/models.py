from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#? 1
# User modeli --> class User(AbstractUser): inherit edilerek yapılmış
# Biz de AbstractUser'dan  inherit ederek kendi User modelimizi oluşturabiliriz.
# Buna exdending user table deniyor,

#? 2
# yeni bir tablo oluşturup, bunu onetoone ile mevcut User tablosuna bağlayarak yapma;
# böylece mevcut User'lara ilave fieldlar ekleyebiliriz.

class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30, blank=True,null=True)
    avatar = models.ImageField(upload_to="pictures",default='pictures/avatar.png')
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"