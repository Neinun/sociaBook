from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def frontpage(request):
    return render(request, 'core/frontpage.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()

    return render(request, 'core/sign_up.html', {'form' : form})


