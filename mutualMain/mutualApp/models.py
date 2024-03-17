from django.db import models

# Create your models here.

class MainDataSet(models.Model):
    scheme_name = models.CharField(max_length=100)
    min_sip = models.IntegerField()
    min_lumpsum = models.IntegerField()
    expense_ratio = models.FloatField()
    fund_size_cr = models.FloatField()
    fund_age_yr = models.IntegerField()
    risk_level = models.IntegerField()
    rating = models.IntegerField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    returns_1yr = models.FloatField()
    returns_3yr = models.FloatField()
    returns_5yr = models.FloatField()

    def __str__(self):
        return self.scheme_name
    

class SelectedData(models.Model):
    scheme_name = models.CharField(max_length=100)
    risk_level = models.IntegerField()
    risk_category = models.CharField(max_length=100)
    returns_1yr = models.FloatField()
    returns_3yr = models.FloatField()
    returns_5yr = models.FloatField()

    def __str__(self):
        return self.scheme_name