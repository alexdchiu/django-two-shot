from django.contrib import admin

# Register your models here.
from receipts.models import Receipt, Account, Category

class ReceiptAdmin(admin.ModelAdmin):
  pass

class AccountAdmin(admin.ModelAdmin):
  pass

class CategoryAdmin(admin.ModelAdmin):
  pass


admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Category, CategoryAdmin)