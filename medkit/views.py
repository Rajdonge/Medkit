from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404, HttpResponse
from .models import Information
from .forms import Medkit_Information
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Landing Page


def home(request):
    return render(request, "home.html")


def create(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(
            request, "Your account has been successfully created.")
        return redirect('loginpage')

    return render(request, "signup.html")

# Login page


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, "home.html")
        else:
            messages.error(request, "Bad Credentials!")
            return redirect("loginpage")

    return render(request, "login.html")

# Register page


# Function: Form to add Medkits


def addMedkit(request):
    if request.method == 'POST':
        addM = Medkit_Information(request.POST)
        if addM.is_valid():
            addM.save()
            # addM = Medkit_Information()
    else:
        addM = Medkit_Information()

    return render(request, "addMedkitForm.html", {'form': addM})


# Display func
def display_data(request):
    total_records = Information.objects.count()
    viewmed = Information.objects.all().order_by('expiry_date')
    if request.method == 'GET':
        st = request.GET.get('servicename')
        if st != None:
            viewmed = Information.objects.filter(medicine_name=st)

    return render(request, "viewMedkit.html", {'viewmed': viewmed, 'total_records': total_records})


# Function to update or edit data
def update_data(request, id):
    if request.method == 'POST':
        up = Information.objects.get(pk=id)
        addM = Medkit_Information(request.POST, instance=up)
        if addM.is_valid():
            addM.save()
    else:
        up = Information.objects.get(pk=id)
        addM = Medkit_Information(instance=up)

    return render(request, "updateMedkit.html", {'form': addM})


# Funtion to delete data
def delete_data(request, id):
    if request.method == 'POST':
        de = Information.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/displaydata')


# Function to sale medkit
def sale(request, id):
    if request.method == 'POST':
        product = Information.objects.get(pk=id)
        product
    return render(request, "sale.html")
