from django.shortcuts import render
from .forms import StudentReg
from django.contrib import messages
# Create your views here.


def reg(request):
    if request.method=='POST':
        fm=StudentReg(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.ERROR,'Your Account has been created successfully !!!')
            #easy way to throw message
            messages.info(request,'you cnt write this here')
    else:
        fm=StudentReg()
    return render(request,'app/userregistration.html',{'form':fm})