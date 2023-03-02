from email import message
from django.core.mail import send_mail
from django.conf import settings

def send_forget_pass(email,token):
  
    subject="Reset  Your Password"
    message=f'click on the link to RESET PASSWORD http://127.0.0.1:8000/changepassword/{token}/'
    from_email= settings.EMAIL_HOST_USER 
    recipient_list=[email]
    send_mail(subject,message,from_email,recipient_list)
    return True