from django.urls import path

from receipts.views import (
  ReceiptListView,
  AccountListView,
  CategoryListView,
)


urlpatterns = [
  path("", ReceiptListView.as_view(), name="receipts_list"),
  path("accounts/", AccountListView.as_view(), name="accounts_list"),
  path("categories/", CategoryListView.as_view(), name="categories_list"),
]