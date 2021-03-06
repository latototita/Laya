from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.views import  View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .home import Index,store
from django.contrib.auth import authenticate, login, logout
from .viewproduct import checkout1
from django.contrib import messages
def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            request.session['customer'] = user.id
            messages.success(request, f'Welcome, {username}.You have Signed In Successfully')
            return redirect('store')
        else:
            messages.success(request, 'Username or Password Incorrect!')
            context={}
            return render(request,'login.html',context)

    context={}
    return render(request,'login.html',context)
'''
class Login(View):
    return_url = None
    def get(self , request):
        customer = request.session.get('customer')
        if customer:
            return redirect('store')

        else:
            Login.return_url = request.GET.get('return_url')
            return render(request , 'login.html')
            

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    
                    Login.return_url = None
                    return redirect('Index')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})
'''

@login_required(login_url='login')
def Logout(request):
    logout(request)
    messages.success(request, 'You have Signed Out Successfully')
    return redirect('store')
