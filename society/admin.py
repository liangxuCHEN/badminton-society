from django.contrib import admin
from society.models import Member, Personal_bill, Bill_table

# Register your models here
class MemberAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'balance')
    fields = ('phone', 'name', 'sexual','balance')

class BillTableAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'comment', 'is_pay')

admin.site.register(Member, MemberAdmin)
admin.site.register(Bill_table, BillTableAdmin)