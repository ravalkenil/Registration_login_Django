from django.urls import path
from newuser import views

urlpatterns = [
    path('',views.user_registration,name="registration"),
    path('login/',views.login_user,name="login"),
    path('home/',views.home,name="home"),
    path('changepassword/<token>/',views.changepassword,name="forgetpassword"),
    path('resetpassword/',views.user_reset_email,name="resetpassword"),
    path('logout/',views.user_logout,name="logout")
]