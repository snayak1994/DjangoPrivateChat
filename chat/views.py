from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("login")

        else:
            return render(request = request,
                          template_name = "registration/register.html",
                          context={"form":form})

    form = UserCreationForm()
    return render(request = request,
                  template_name = "registration/register.html",
                  context={"form":form})


