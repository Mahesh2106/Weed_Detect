from django.shortcuts import render,redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from keras.applications.imagenet_utils import preprocess_input
from django.contrib import messages
from PIL import Image
from Frontend.models import Review,Registration
from django.http import HttpResponse,JsonResponse
import io


def home(request):
    x=Review.objects.all()
    return render(request,'Home.html',{'x':x})


def detect_weed_or_crop(request):
    if request.method == 'POST':
        try:
            model = load_model('weed_model.h5')

            img_data = request.FILES.get('image_file')



            img = Image.open(io.BytesIO(img_data.read()))

            img = img.resize((224, 224))

            x = image.img_to_array(img)
            x = x / 255.0
            x = np.expand_dims(x, axis=0)

            # Make predictions
            preds = model.predict(x)
            preds = np.argmax(preds, axis=1)

            result = "weed detected" if preds == 1 else "crop detected"
            messages.success(request,result)
        except Exception as e:
            messages.error(request,e)

    return redirect(home)

def ReviewSave(req):
    if req.method=="POST":
        nm=req.POST.get('uname')
        des=req.POST.get('txt')
        x=Review(username=nm,Description=des)
        x.save()
        messages.success(req,"Review Submitted Successfully")
        return redirect(home)

def RegistrationForm(req):
    return render(req,"Registration.html")



def Registration_save(request):
    if request.method == "POST":
        nm = request.POST.get('uname')
        em = request.POST.get('email')
        passw = request.POST.get('password')
        con = request.POST.get('cpassword')
        if passw != con:
            messages.error(request, "Password and confirm password do not match.")
            return redirect(RegistrationForm)
        registration = Registration(username=nm, Email=em, Password=passw, Confirm_Password=con)
        registration.save()
        messages.success(request,"Registered Succesfully")
        return redirect(Login_Pg)

def Login_Pg(req):
    return render(req,"Login_Pg.html")

def Login_fun(request):
    if request.method=="POST":
        nm=request.POST.get('uname')
        pwd=request.POST.get('password')
        if Registration.objects.filter(username=nm,Password=pwd).exists():
            request.session['username']=nm
            request.session['Password']=pwd
            messages.success(request, "Logged in Successfully")
            return redirect(home)
        else:
            messages.warning(request, "Check Your Credentials")
            return redirect(Login_Pg)
    else:
        messages.warning(request, "Check Your Credentials Or Sign Up ")
        return redirect(Login_Pg)

def Logout_fn(request):
    del request.session['username']
    del request.session['Password']
    messages.success(request, "Logged Out Successfully")
    return redirect(Login_Pg)