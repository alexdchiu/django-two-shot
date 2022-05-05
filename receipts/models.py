from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.
class Receipt(models.Model):
  vendor = models.CharField(max_length = 200)
  total = models.DecimalField(decimal_places=3, max_digits=10)
  tax = models.DecimalField(decimal_places=3, max_digits=10)
  date = models.DateField()
  category = models.ForeignKey("Category",related_name="receipts", on_delete=models.CASCADE)
  account = models.ForeignKey("Account", related_name="receipts", on_delete=models.CASCADE, null = True)
  owner = models.ForeignKey(USER_MODEL,related_name="receipts", on_delete=models.CASCADE)

  def __str__(self):
    return str(self.vendor) + " - " + str(self.date)

class Account(models.Model):
  name = models.CharField(max_length=100)
  number = models.PositiveSmallIntegerField()
  owner = models.ForeignKey(USER_MODEL,related_name="accounts", on_delete=models.CASCADE)

  def __str__(self):
    return str(self.name)

class Category(models.Model):
  name = models.CharField(max_length=100)
  owner = models.ForeignKey(USER_MODEL,related_name="categories", on_delete=models.CASCADE)

  def __str__(self):
    return str(self.name)
