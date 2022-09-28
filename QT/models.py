from django.db import models


# Create your models here.
class Developers(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Dev_id = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)


class Managers(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Manager_id = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)


class Report(models.Model):
    Project_Name = models.CharField(max_length=20)
    Dev_Name = models.CharField(max_length=20)
    Project_Report = models.CharField(max_length=2000)
    Status = models.BooleanField(default=False)


class AssignedWork(models.Model):
    Project_Name = models.CharField(max_length=20)
    Work_To_Do = models.CharField(max_length=200)
