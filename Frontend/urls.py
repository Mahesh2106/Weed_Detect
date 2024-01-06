from django.urls import path
from Frontend import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('detect_weed_or_crop/',views.detect_weed_or_crop,name="detect_weed_or_crop"),

    path('ReviewSave/',views.ReviewSave,name="ReviewSave"),
    path('RegistrationForm/',views.RegistrationForm,name="RegistrationForm"),

    path('Registration_save/',views.Registration_save,name="Registration_save"),
    path('Login_Pg/',views.Login_Pg,name="Login_Pg"),

    path('Login_fun/',views.Login_fun,name="Login_fun"),
    path('Logout_fn/',views.Logout_fn,name="Logout_fn"),
]