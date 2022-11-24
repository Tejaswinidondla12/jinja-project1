from django.shortcuts import render

# Create your views here.
def Teju(request):
    d={'name':'honey','age':22}
    return render(request,'Teju.html',d)
    
