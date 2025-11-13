from django.shortcuts import render, redirect
from .forms import RegistrationForms
from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView,ListView
from django.urls import reverse_lazy
from .models import Registration 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '1234':
            return redirect('result_view')  
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    

    return render(request, 'login.html')

class ResultView(TemplateView):
    template_name = "result.html"


class RegisterListView(ListView):
    model = Registration                       
    template_name = "list.html"                 
    context_object_name = "registrations"         


class RegisterCreateView(CreateView):
    model = Registration
    fields = ['first_name', 'last_name', 'email', 'phone', 'gender']
    template_name = "create.html"
    success_url = reverse_lazy('list')


class RegisterUpdateView(UpdateView):
    model = Registration
    fields = ['first_name', 'last_name', 'email', 'phone', 'gender']
    template_name = "update.html"
    success_url = reverse_lazy('list')


class RegisterDeleteView(DeleteView):
    model = Registration
    template_name = "delete.html"
    success_url = reverse_lazy('list')


def result_view(request):
    return render(request, 'result.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'name': form.cleaned_data['first_name']})
    else:
        form = RegistrationForms()
    return render(request, 'register.html', {'form': form})