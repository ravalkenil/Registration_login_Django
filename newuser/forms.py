from dis import show_code
from django import forms
import re

#password validation function
def is_password_strong_enough(password):
    hit = re.match("^.*(?=.{6,})(?=.*\d)(?=.*[A-Z]).*$", password)
    return bool(hit)

#registration form
class registration(forms.Form):
    first_name=forms.CharField(error_messages ={'required':"Please Enter your First name"}, label='Firstname')
    last_name=forms.CharField(error_messages ={'required':"Please Enter your Last name"}, label='Lastname')
    email=forms.EmailField(required=True,error_messages ={'required':"Please enter your valid Email"}, label='Email')
    password= forms.CharField(widget=forms.widgets.PasswordInput,show_hidden_initial=show_code, label='Password')
    confirm_password = forms.CharField(widget = forms.PasswordInput, label='Confirm Password')
    def __init__(self, *args, **kwargs):
        super(registration, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['style'] = 'margin-bottom:8px'
               
#login form
class user_login(forms.Form):
    email=forms.EmailField(required=True,error_messages ={'required':"Please enter your valid email"},label='Email')
    password = forms.CharField(widget = forms.PasswordInput,error_messages ={'required':"enter your password"},label='Password')
    def __init__(self, *args, **kwargs):
        super(user_login, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
#change password form
class forget(forms.Form):
    email=forms.EmailField(required=True,error_messages ={'required':"Please enter your valid email"},label='Email')
    password=forms.CharField(widget = forms.PasswordInput,error_messages ={'required':"enter your password"},label='Password')
    confirm_password = forms.CharField(widget = forms.PasswordInput,error_messages ={'required':"enter your re  password"},label='Confirm Password')
    def __init__(self, *args, **kwargs):
        super(forget, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

#forget for email form
class reset_password_email(forms.Form):
    email=forms.EmailField(required=True,error_messages ={'required':"Please enter your valid email"})
    def __init__(self, *args, **kwargs):
        super(reset_password_email, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


