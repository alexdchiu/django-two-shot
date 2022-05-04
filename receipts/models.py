from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.
class Receipt(models.Model):
  vendor = models.CharField(max_length = 100)
  total = models.DecimalField(decimal_places=2, max_digits=10)
  tax = models.DecimalField(decimal_places=3, max_digits=4)
  date = models.DateField()
  category = models.ForeignKey("Category", on_delete=models.PROTECT)
  account = models.ForeignKey("Account", on_delete=models.PROTECT)
  owner = models.ForeignKey(USER_MODEL,related_name="receipts", on_delete=models.CASCADE)

  def __str__(self):
    return str(self.vendor) + " - " + str(self.date)