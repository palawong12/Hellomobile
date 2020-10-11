from django.contrib import admin
from .models import ReportList, AllCustomer, Profile, DocumentUpload, Contact
admin.site.register(ReportList)

class CustomerAdmin(admin.ModelAdmin):
	list_display = ['level','customer_id','customer_name','customer_tel','other']
	list_filter = ['level']
	list_editable = ['customer_name','customer_tel','other']


admin.site.register(AllCustomer, CustomerAdmin)
admin.site.register(Profile)
admin.site.register(DocumentUpload)
admin.site.register(Contact)