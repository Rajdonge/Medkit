from django.db import models

# Create your models here.


class Information(models.Model):
    medicine_name = models.CharField(max_length=30)
    expiry_date = models.DateField(
        error_messages={'invalid': 'Please enter in "YYYY-MM-DD" Format!'})
    quantity = models.IntegerField(
        error_messages={'invalid': 'Please enter numbers!'})
    marked_price = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    discount = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    company = models.CharField(max_length=30)
    dealer = models.CharField(max_length=30)


class Sale_Information(models.Model):
    medicine_name = models.CharField(max_length=30)
    quantity = models.IntegerField(
        error_messages={'invalid': 'Please enter numbers!'})
    marked_price = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    discount = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    sale_id = models.ForeignKey(Information, on_delete=models.CASCADE)
