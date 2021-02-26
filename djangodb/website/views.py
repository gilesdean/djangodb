from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages


# Create your views here.

def home(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            age = request.POST['age']
            email = request.POST['email']
            passwd = request.POST['passwd']

            messages.success(request, ('There was an error in your form.'))
            #return redirect('join')
            return render(request, 'home.html', {'fname':fname, 
                'lname':lname, 
                'age':age,
                'email':email,
                'passwd': passwd,
                })
        messages.success(request, ('Your Form Has Been Submitted Successfully!'))
        return redirect('home')

    else:
        return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})