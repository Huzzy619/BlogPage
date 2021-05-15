from django.shortcuts import render , redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from .forms import NameForm

# Create your views here.


def register (request):
	if request.method == 'POST':
		form = UserRegisterForm (request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username} You can now Login !')
			return redirect('login')
	else:	

		form = UserRegisterForm ()

	return render(request , 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Profile is updated')
			return redirect('profile')
		
	else: 
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance  =request.user.profile)


	context = {

	'u_form':u_form,
	'p_form':p_form

	}



	return render(request , 'users/profile.html', context)




def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST,)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def home_view(request):
	print(request.GET)
	return render(request, 'users/name.html')  