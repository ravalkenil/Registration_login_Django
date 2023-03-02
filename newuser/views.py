# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import registration, user_login,forget,reset_password_email
from newuser.models import registration_model
from django.contrib import messages
from .helper import send_forget_pass
import uuid
import re
from django.views.decorators.cache import cache_control 

## password validation function
def is_password(password):
    hit = re.match("^.*(?=.{8,})(?=.*\d)(?=.*[A-Z])(?=.*@).*$", password)
    return bool(hit)

###  new user 
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def user_registration(request):
    if request.method=='POST':
        if request.session.get('email') == None:
            fm=registration(request.POST)
            
            if fm.is_valid():
                    firstname=request.POST.get('first_name')
                    lastname=request.POST.get('last_name')
                    email=request.POST.get('email')
                    password=request.POST.get('password')
                    re_password=request.POST.get('confirm_password') 
                    if registration_model.objects.filter(f_email=email).exists():
                        messages.error(request,'Email Is  Alredy Exits')
                    else:
                        if password and not is_password(password):
                            messages.error(request,'Passwords must be at least 8 characters long  with at least 1 upper-case letter,lower-case letter and 1 number.')
                        else:
                            if password == re_password:
                                en=registration_model(first_name=firstname,last_name=lastname,f_email=email,password=re_password)
                                en.save()
                                request.session['email']=email
                                return redirect('home')
                            else:
                                messages.error(request,"Password and confirm password are not the same")
        
        else:
            return redirect('home')
    else:
        if request.session.get('email') and request.session.get('email') != None:
            return redirect('home')
            
        else:
            fm=registration()
    data={'form':fm,}
    return render(request,'newuser.html',data)

##  login user 
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login_user(request):

    if request.method=='POST':
        
        if request.session.get('email') == None:
            fm = user_login(request.POST)
            
            if fm.is_valid():
                email=request.POST.get('email')
                password=request.POST.get('password')
                if registration_model.objects.filter(f_email=email).exists():
                    if registration_model.objects.filter(f_email=email,password=password).exists():
                        request.session['email']=email
                        ip = request.META.get('REMOTE_ADDR')
                        print(ip)
                        return redirect('home')
                    else:
                        messages.error(request,'Invalid password')
                else:
                    messages.error(request,'Email is not exists')
            else:
                messages.error(request,'Invalid email and password')
        else:
            return redirect('home')
    else:
        if request.session.get('email') and request.session.get('email') != None:
            return redirect('home')
        else:
            fm=user_login()
    data1={ 
        'login':fm,
    }
    return render(request,'login_user.html',data1)
            

#home
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def home(request):
    name=request.session.get('email')
    if request.session.get('email') and request.session.get('email') != None:
        
        return render(request,'home.html',{'name':name})
    else:
        return HttpResponseRedirect('/login/')

#forget password
def changepassword(request,token):
    fm=forget()
    data={
        'form':fm
    }
    if request.method=='POST':
        fm=forget(request.POST)
        if fm.is_valid():
            email=request.POST.get('email')
            password=request.POST.get('password')
            re_password=request.POST.get('confirm_password')
            if registration_model.objects.filter(f_email=email).exists():
                if password and not is_password(password):
                    messages.error(request,'Passwords must be at least 8 characters long  with at least 1 upper-case letter,lower-case letter and 1 number.')
                else:
                    if registration_model.objects.filter(password=password).exists():
                    
                        messages.error(request,'Password should not be same as old password')
                    else:
                        if password==re_password:
                            en=registration_model.objects.get(f_email=email)
                            en.password=re_password
                            en.save()
                            messages.success(request,'Password changed sucessfully')
                            return HttpResponseRedirect('/login/')
                        else:
                            messages.error(request,'Password and confirm password are not the same')
            else:
                messages.error(request,'email is not exists')
    else:
        fm=forget()
    data={
        'form':fm
    }

    return render(request,'changepassword.html',data)

#forget password with email
def user_reset_email(request):
    fm=reset_password_email()
    data={
        'form':fm
    }
    if request.method=='POST':
        user_email=request.POST.get('email')
        if registration_model.objects.filter(f_email=user_email).exists():
            email=request.POST.get('email')
            token=str(uuid.uuid4())
            send_forget_pass(email,token)
            messages.success(request,'Email sent successfully')
            return redirect('/resetpassword/')
        else:
            messages.error(request,'Email is not exists')
            return redirect('/resetpassword/')
     
    return render(request,'forget_.html',data)

def user_logout(request):
    request.session.flush()
    return redirect('login')
