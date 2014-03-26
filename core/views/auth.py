from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render_to_response
from django.core.context_processors import csrf
from core.models import Employee

def login_view(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.            
                return redirect('/')
            else:
                # Return a 'disabled account' error message
                return redirect('/account-disabled')
        else:
            # Return an 'invalid login' error message.
            return redirect('/login-failed')
    else:
        #next = request.GET['next']
        return render_to_response('core/login.html', c)
        
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')

def changePassword(request):
    # TO-DO
    return redirect('/password-changed')
    
def createUser_view(request):
    c = {}
    c.update(csrf(request))
    if request.POST:    
        username = request.POST['username']
        password = request.POST['password']
        Employee.objects.create_employee(username, password)
        return redirect('/')
    else:
        return render_to_response('core/create_user.html', c)