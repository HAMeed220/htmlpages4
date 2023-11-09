from django.shortcuts import render


# Create your views here.

def msg(request):
    return render(request,'msg.html')
def hello(request):
    return render(request,'hello.html')
def base(request):
    return render(request,'base.html')
def exm(request):
    return render(request,'exm.html')