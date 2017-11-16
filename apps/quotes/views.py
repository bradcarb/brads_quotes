from __future__ import unicode_literals
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages
from .models import User, Quote

def index(request):
    return render(request,'quotes/index.html')

def home(request): 
            
    context = {
        'all_users':User.objects.all(),
        'all_quotes':Quote.objects.all(),
        'user':User.objects.get(id=request.session['user_id'])
        # 'user':User.objects.get(id=request.session['user_id'])
    }
    # print User.objects.first()
    # print request.POST['email']
    return render(request, 'quotes/home.html', context)

def user(request):
    context = {
        'user':User.objects.get(id=user_id)
    }
    return render(request,'quotes/user.html', context)

def register(request):
    result = User.objects.register(request.POST)

    if result[0]:
        request.session['user_id'] = request.POST['user_id']
        return redirect('/home')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect('/')

def login(request):
    result = User.objects.login(request.POST)
    request.session['user_id'] = result[1].id
    # user_id=request.session['user_id']

    if result[0]:
        # User.objects.get(email=POST['email'])
        # print User.objects.get(id=1)
        # print user_id
        # print request.POST['id']
        return redirect('/home')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
            # request.session['user_id'] = result.id
        return redirect('/')

def quote(request):
    
    result = Quote.objects.quote(request.POST)
    if result[0]:
        return redirect('/home')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)
            # request.session['user_id'] = result.id
        return redirect('/home')

def favorite(request):
    return redirect('/home')

def unfavorite(request):
    return redirect('/home')