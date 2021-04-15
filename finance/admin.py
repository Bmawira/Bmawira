from django.contrib import admin
from finance.models import Allowance, Deduction, Payroll, PaySlip, Bank, BankBranch, PettyCash, Expenditure

# Register your models here.
admin.site.register(Allowance)
admin.site.register(Deduction)
admin.site.register(Payroll)
admin.site.register(PaySlip)
admin.site.register(Bank)
admin.site.register(BankBranch)
admin.site.register(PettyCash)
admin.site.register(Expenditure)
