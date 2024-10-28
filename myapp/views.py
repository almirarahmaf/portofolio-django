from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'myapp/profile.html')

def qualification(request):
    return render(request, 'myapp/qualification.html')

def experience(request):
    return render(request, 'myapp/experience.html')

def contact(request):
    return render(request, 'myapp/contact.html')