from django.db import models


class Banks(models.Model):
    name = models.CharField(max_length=49)
    id = models.BigAutoField(primary_key=True)


class Branches(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)


class BankBranches(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)

    class Meta:
        managed = False
        db_table = 'bank_branches'
