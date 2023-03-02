

from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from .models import registration_model
# from .forms import user_login
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in,sender=registration_model)
def login_success(sender,request,user,**kwargs):
    print("_____________________")
    ip=request.META.get('REMOTE_ADDR') 
    print("id:",ip) 

    user_logged_in.connect(login_success,sender=registration_model)

# @receiver(user_logged_in,sender=User)
# def  login_success(sender,request,user,**kwargs):
#     ct=cache.get('count',0,version=user.pk)
#     newcount=ct +1
#     cache.set('count',newcount,60*24,version=user.pk)
#     print(user.pk)


# Learned how to use signals and built in signals in Django and how to use login logout signals, model signals, request-response signals and management signals.
# learned how to track user ip address in django
# Learned how to count the number of times a user logs into a web page using signals in django and learned how to use custom signal in django