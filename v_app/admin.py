from django.contrib import admin
from .models import Category,Product,Order,ContactMessage,Medicines,PharmLab

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Medicines)
admin.site.register(PharmLab)

class OrderAdmin (admin.ModelAdmin):
    list_display = ('id','cus_name','cus_phone' ,'cus_email','pro_name','order_date','order_on')
admin.site.register(Order,OrderAdmin)



class ContactAdmin (admin.ModelAdmin):
    list_display = ('id','name','last_name' ,'email','phone_number','subject','message','image')
admin.site.register(ContactMessage,ContactAdmin)