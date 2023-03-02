from django.contrib import admin
from newuser.models import registration_model

# Register your models here.
class contectadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','f_email','password')
    
admin.site.register(registration_model,contectadmin)