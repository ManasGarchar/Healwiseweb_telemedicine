from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from django.http import HttpResponse
from .models import Feedback  # Import your Feedback model


from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

from django.shortcuts import render, redirect
from .models import Appointment

from django.shortcuts import render, redirect
from .models import Appointment

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import Appointment
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Appointment

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Appointment
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from django.http import HttpResponse
from .models import Appointment
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    all_appointments = Appointment.objects.filter(user_id=user)
    return render(request, 'profile.html', {'user': user, 'all_appointments': all_appointments})




@login_required
def submit_appointment(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            try:
                # Get the user associated with the current session
                user = request.user

                # Create a new Appointment object and associate it with the logged-in user
                appointment = form.save(commit=False)
                appointment.user_id = user
                appointment.save()

                # Redirect to a success page
                return redirect('about')  # Redirect to a success page

            except Exception as e:
                # Handle any exceptions that might occur
                return HttpResponse(f'An error occurred: {e}')
        else:
            # Form is not valid, render the appointment form page with errors
            return render(request, 'appointmenthospital.html',  {'user': request.user})

    # If the request method is not POST, render the empty appointment form page
    form = AppointmentForm()
    return render(request, 'appointmenthospital.html', {'form': form})



def review(request):

    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        try:
            # Extract form data from the request
            name = request.POST.get('uname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('msg')

            # Create a new Feedback object and save it to the database
            feedback = Feedback.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )

           

            # Return a success response or redirect to a success page
            return redirect('about')  # Redirect to a success page

        except Exception as e:
            # Handle any exceptions that might occur
            return HttpResponse(f'An error occurred: {e}')

    # If the request method is not POST, render the feedback page
    return render(request, 'review.html')





def singup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            return render(request, 'singup.html', {'error': 'Passwords do not match'})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'singup.html', {'error': 'Username already exists'})

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'singup.html', {'error': 'Email already exists'})

        # Create user
        obj = User.objects.create_user(username=username, email=email, password=password1)
        obj.save()
        return redirect('login')

    return render(request, 'singup.html')


def about(request):
    
    return render(request,'home.html')
       

from django.contrib import auth

def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('about')  # Redirect to the about page after successful login
        else:
            # Handle invalid credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('about')  # Redirect to the homepage after logout

def introduction(request):
    return render(request,'introduction.html')

def us(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def minor(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'minor.html')



def appointmenthospital(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'appointmenthospital.html')

def intermediate(request):
    return render(request,'intermediate.html')

def severe(request):
    return render(request,'severe.html')

def question_general(request):
    return render(request,'question_general.html')

def que_ent(request):
    return render(request,'que_ent.html')

def que_gynac(request):
    return render(request,'que_gynac.html')

def que_orthopedist(request):
    return render(request,'que_orthopedist.html')

def que_skin(request):
    return render(request,'que_skin.html')

def que_dentist(request):
    return render(request,'que_dentist.html')

