from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from receipts.models import Receipt,

# Create your views here.
class ReceiptListView(ListView):
  model = Receipt
  template_name = "receipts/list.html"
  context_object_name = "receiptlists"

  # def get_queryset(self):
  #   return Receipt.objects.filter(owner=self.request.user)