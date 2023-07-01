from django.contrib import admin
from CustomerServiceRequest.models import Customer_Service_Request, OrderCheckout


# Register your models here.
class CustomerServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("CSR_name", "CSR_email", "CSR_phone", "CSR_Subject", "CSR_message")


class OrderCheckoutAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "address", "phone", "city", "State")


admin.site.register(Customer_Service_Request, CustomerServiceRequestAdmin)

admin.site.register(OrderCheckout, OrderCheckoutAdmin)
