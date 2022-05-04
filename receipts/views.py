from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from receipts.models import Receipt, Account

# Create your views here.
class ReceiptListView(ListView):
  model = Receipt
  template_name = "receipts/list.html"
  context_object_name = "receiptslist"

  # def get_queryset(self):
  #   return Receipt.objects.filter(owner=self.request.user)


class AccountListView(LoginRequiredMixin, ListView):
  model = Account
  template_name = "receipts/accounts.html"
  context_object_name = "accountlists"

  # def get_queryset(self):
  #   return Account.objects.filter(owner=self.request.user)