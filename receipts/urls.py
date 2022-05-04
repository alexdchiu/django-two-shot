from django.urls import path
from receipts.models import Account

from receipts.views import (
  ReceiptListView,
  AccountListView,
  CategoryListView,
  ReceiptCreateView,
  AccountCreateView,
)


urlpatterns = [
  path("", ReceiptListView.as_view(), name="receipts_list"),
  path("accounts/", AccountListView.as_view(), name="accounts_list"),
  path("categories/", CategoryListView.as_view(), name="categories_list"),
  path("create/", ReceiptCreateView.as_view(), name="receipt_create"),
  path("accounts/create/", AccountCreateView.as_view(), name="account_create"),
]