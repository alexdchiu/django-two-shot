from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from receipts.models import Receipt, Account, Category

# Create your views here.
class ReceiptListView(ListView):
  model = Receipt
  template_name = "receipts/list.html"
  context_object_name = "receiptslist"

  def get_queryset(self):
    return Receipt.objects.filter(owner=self.request.user)


class AccountListView(LoginRequiredMixin, ListView):
  model = Account
  template_name = "receipts/accounts.html"
  context_object_name = "accountslist"

  def get_queryset(self):
    return Account.objects.filter(owner=self.request.user)

class CategoryListView(LoginRequiredMixin, ListView):
  model = Category
  template_name = "receipts/categories.html"
  context_object_name = "categorieslist"

  def get_queryset(self):
    return Category.objects.filter(owner=self.request.user)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
  model = Receipt
  template_name = "receipts/create.html"
  fields = ["vendor", "total", "tax", "date", "category", "account"]
  success_url = reverse_lazy("receipts_list")

  def form_valid(self, form):
    form.instance.purchaser = self.request.user
    return super().form_valid(form)

class AccountCreateView(LoginRequiredMixin, CreateView):
  model = Account
  template_name = "receipts/accounts/create.html"
  fields = ["name", "number"]
  success_url = reverse_lazy("accounts_list")

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

class CategoryCreateView(LoginRequiredMixin, CreateView):
  model = Category
  template_name = "receipts/categories/create.html"
  fields = ["name"]
  success_url = reverse_lazy("categories_list")

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)