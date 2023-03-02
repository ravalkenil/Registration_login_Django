

from django.db import models

# Create your models here.
class registration_model(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    f_email=models.EmailField(max_length=35)
    password=models.CharField(max_length=10)

    def isexists(self):
        if registration_model.objects.filter(email = self.f_email):
            return True
        return False