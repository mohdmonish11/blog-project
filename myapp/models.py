from django.db import models

# Create your models here.
class Sign_up(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    class Meta:
        db_table = "user_table"

class Create_article(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    class Meta:
        db_table = "createpost"