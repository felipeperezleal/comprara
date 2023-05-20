from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def change_password(request):
    user = User.objects.get('username')
    if request.POST.get('pswd') == request.POST.get('pswd2'):
        user.set_password(request.POST['pswd'])
        user.save()
        return redirect('profile')
    else:
        messages.error(request, 'Las contraseñas no coinciden')
        return render(request, 'register.html')