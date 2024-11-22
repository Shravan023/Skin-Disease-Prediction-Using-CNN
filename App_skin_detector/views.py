from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import*
import keras
import operator
from keras.preprocessing import image
# import keras.utils as image
from keras.models import model_from_json
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from PIL import Image
import io
from tensorflow.keras.utils import img_to_array
import os
from tensorflow.keras.models import load_model
from django.conf import settings
import tensorflow as tf
import os
import numpy as np
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from django.db.models import Q

# Ensure the model is loaded properly
model_path = os.path.join(settings.BASE_DIR, 'my_model_10.h5')

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file {model_path} does not exist.")
# Create your views here.

class_names = [
    "Acne and Rosacea Photos",  # Acne and Rosacea
    "Atopic Dermatitis Photos",  # Atopic Dermatitis
    "Eczema Photos",  # Eczema
    "Hair Loss Photos Alopecia and other Hair Diseases",  # Alopecia
    "Psoriasis pictures Lichen Planus and related diseases",  # Psoriasis
    "Seborrheic Keratoses and other Benign Tumors",  # Seborrheic Keratosis
    "Tinea Ringworm Candidiasis and other Fungal Infections",  # Fungal Infections
    "Urticaria Hives"  # Urticaria (Hives)
]
num_classes = len(class_names)
# Inputs and rescaling


model = load_model(model_path,compile = False)
def Home(request):
	return render(request,"Home.html",{})

# This function handles the image upload and prediction
def Upload_image(request):
    if request.method == "POST":
        # Ensure 'image' exists in the request
        if 'image' not in request.FILES:
            messages.error(request, "No image uploaded.")
            return render(request, "Upload_image.html", {})

        # Get the uploaded image
        uploaded_image = request.FILES['image']
        
        # Create a safe path for storing the uploaded image
        upload_folder = os.path.join(settings.BASE_DIR, 'uploads')
        os.makedirs(upload_folder, exist_ok=True)

        image_path = os.path.join(upload_folder, uploaded_image.name)
        
        # Save the uploaded image
        fs = FileSystemStorage(location=upload_folder)
        with fs.open(uploaded_image.name, 'wb') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

        # Load and preprocess the image
        img = image.load_img(image_path, target_size=(120, 120))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)  # Add batch dimension
        x /= 255.0  # Normalize pixel values

        # Make a prediction with the loaded model
        predictions = model.predict(x)

        # Get the predicted class
        predicted_class_index = np.argmax(predictions)
        predicted_class_name = class_names[predicted_class_index]
        print(predicted_class_name)
        detected =  predicted_class_name
        messages.info(request,'Detected Class is' +' '+predicted_class_name +'.Redirecting to medicines page')

        # Get medicine details based on the predicted class
        from .models import medicine_detail
        details = medicine_detail.objects.filter(medicine_on=detected)

        # Return the results to a rendered template
        return render(request, "Medicine.html", {'details': details, 'detected': detected})

    # If not POST, render the upload image page
    return render(request, "Upload_image.html", {})

def Medicine(request):
    return render(request,"Medicine.html",{})


def View_doctors(request):
    details = Doctor_detail.objects.all()
    return render(request, "View_doctors.html", {'details': details})


def Admin_Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if AdminDetails.objects.filter(username = username,password = password).exists():
            ad = AdminDetails.objects.get(username=username, password=password)
            print('d')
            messages.info(request,'Admin login is Sucessfull')
            request.session['type_id'] = 'Admin'
            request.session['UserType'] = 'Admin'
            request.session['login'] = "Yes"
            return redirect("/")
        else:
            print('y')
            messages.error(request, 'Error wrong username/password')
            return render(request, "Admin_Login.html", {})
    else:
        return render(request, "Admin_Login.html", {})


def Register(request):
    # data = login.objects.all().filter(email=email,password=password)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print('name', name)
        print('email',email)
        print('username',username)
        print('password',password)
        print('confirm_password',confirm_password)
        Data = loggedin(name=name,email=email,username=username,password=password,confirm_password=confirm_password)
        Data.save()
        return redirect("/login/")
    else:
        return render(request,'registration.html',{})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        print('username',username)
        print('password',password)
        if loggedin.objects.all().filter(username=username,password=password).exists():
            Data = loggedin.objects.all().filter(username=username, password=password )
            for i in Data:
                User_id = i.id
            # print('login')
            request.session['User_ID'] = User_id
            request.session['type_id'] = 'User'
            request.session['login'] = "Yes"
            return redirect('/')
        else:
            print("Please Register first")
            return redirect('/register/')
    return render(request,'login.html',{})

def Logout(request):
    Session.objects.all().delete()
    return redirect("/")

def feedback(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        mailid=request.POST['mailid']
        feedback=request.POST['subject']
        print('firstname',firstname)
        print('lastname',lastname)
        print('mailid',mailid)
        print('feedback',feedback)
        Data= Feedback_details(firstname=firstname,lastname=lastname,mailid=mailid,feedback=feedback)
        Data.save()
        messages.info(request,"Thank you for Feedback")
        return redirect("/")
    else:
        return render(request,"feedback.html",{})

def View_feedback(request):
    details = Feedback_details.objects.all()
    return render(request,"View_feedback.html",{'details':details})

def View_Doctors2(request):
    details = Doctor_detail.objects.all()
    return render(request,"view_doctors2.html",{'details':details})

def Update_Doctor(request):
    if request.method =="POST":
        Doctor_detail_ID = request.POST['1updateid']
        name=request.POST['1updatename']
        Gender=request.POST['1updategender']
        Speciality=request.POST['Speciality_In']
        Department=request.POST['1updateDepartment']
        Doctor_detail.objects.filter(id = Doctor_detail_ID).update(
                                                        name=name
                                                        ,Gender=Gender
                                                        ,Speciality=Speciality
                                                        ,Department=Department)
        messages.info(request,"Doctor Details Updated")
        return redirect('/View_doctors/')
    else:
        return render(request,"View_doctors.html",{})

def Add_Doctor(request):
    if request.method == "POST":
        name = request.POST['name']
        Gender = request.POST['Gender']
        print(Gender)
        Speciality = request.POST['Speciality']
        Department = request.POST['Department']
        obj = Doctor_detail(
                        name         = name
                        ,Gender      = Gender
                        ,Speciality  = Speciality
                        ,Department  = Department
                    )
        obj.save()
        messages.info(request,"Doctor details Sucessfully Added")
        return redirect("/View_doctors/")
    else:
        return render(request,"Add_doctor.html",{})

def delete_doctor(request,id):
    Doctor_detail.objects.filter(id=id).delete()
    return redirect('/View_doctors/')

def View_Users(request):
    details = loggedin.objects.all()
    return render(request,"view_user.html",{'details':details})

def Add_Medicine(request):
    if request.method == "POST":
        medicine_name = request.POST['medicine_name']
        medicine_on = request.POST['medicine_on']
        medicine_type = request.POST['medicine_type']
        print(medicine_on)
        description = request.POST['description']
        price = request.POST['price']
        obj = medicine_detail(
                        medicine_name = medicine_name
                        ,medicine_on  = medicine_on
                        ,medicine_type = medicine_type
                        ,description = description
                        ,price        = price
                    )
        obj.save()
        messages.info(request,"Medicinal details Sucessfully Added")
        return redirect("/manage_medicine/")
    else:
        return render(request,"Add_medicine.html",{})

def manage_medicine(request):
    details = medicine_detail.objects.all()
    return render(request, "manage_medicine.html", {'details': details})

def View_Medicine(request):
    details = medicine_detail.objects.all()
    return render(request, "manage_medicine.html", {'details': details})


def Update_Medicine(request):
    if request.method =="POST":
        medicine_detail_ID = request.POST['update_id']
        medicine_name=request.POST['update_medicinename']
        medicine_on=request.POST['medicine_in']
        medicine_type = request.POST['medicine_of']
        description = request.POST['medicine_can']
        price=request.POST['update_price']
        medicine_detail.objects.filter(id = medicine_detail_ID).update(
                                                        medicine_name = medicine_name
                                                        ,medicine_on  = medicine_on
                                                        ,medicine_type = medicine_type
                                                        ,description = description
                                                        ,price        = price)
        messages.info(request,"Medicinal Details Updated")
        return redirect('/manage_medicine/')
    else:
        return render(request,"manage_medicine.html",{})

def delete_medicine(request,id):
    medicine_detail.objects.filter(id=id).delete()
    return redirect('/manage_medicine/')


def View_Doctors_New(request,detected):
    print(detected)
    details= Doctor_detail.objects.filter(Speciality=detected)
    return render(request,'Doctors.html',{'details':details,'detected':detected})



