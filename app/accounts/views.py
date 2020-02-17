from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from accounts.models import App
# Create your views here.
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    app_lists = App.objects.all()
    app_user_counts = App.objects.annotate(num_apps=Count('name'))
    params = {
        'app_lists': app_lists,
        'app_user_counts': app_user_counts
    }

    return render(request, 'dashboard.html', params)

def registerView(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else :
        form=UserCreationForm()

    return render(request, 'registration/register.html',{'form':form})