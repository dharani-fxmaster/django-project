from django.shortcuts import render
from . models import UserProfile

def index(request):
    login = UserProfile()
    return render(request, "index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Simple check against stored users (not secure for production)
        try:
            user = UserProfile.objects.get(username=username, password=password)
            # If found, redirect to registration page
            return redirect('register')
        except UserProfile.DoesNotExist:
            # If login fails, show error
            return render(request, 'index.html', {'error': 'Invalid username or password'})

    return render(request, 'index.html')


def register_view(request):
    return render(request, 'register.html')