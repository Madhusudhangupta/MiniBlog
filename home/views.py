from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group

def home(request):
    posts = Post.objects.all()
    return render(request, 'home/home.html', {'posts':posts})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'home/dashboard.html', {'name':request.user, 'posts':posts, 'full_name':full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('login')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully!!!')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(request, username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successsfully')
                    return HttpResponseRedirect('dashboard')
        else:
            form = LoginForm()
            print(form.data)
        return render(request, 'home/login.html', {'form':form})
    else:
        return HttpResponseRedirect('dashboard')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                # form = PostForm()
                return HttpResponseRedirect('dashboard')
        else:
            form = PostForm()
        return render(request, 'home/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('login')

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'home/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('login')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('dashboard')
    else:
        return HttpResponseRedirect('login')




'''
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully!!!')
            form.save()
            # return HttpResponseRedirect('login')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form':form})

def user_login(request):
    # if not request.user.is_authenticated:
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, pasword=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in as {username}.')
                return HttpResponseRedirect('dashboard')
            else:
            #     form = LoginForm()
            # return render(request, 'home/login.html', {'form':form})
                messages.error(request, "Invalid username or password.")
        else:
            # return HttpResponseRedirect('dashboard')
            messages.error(request, "Invalid username or password.")
    form = LoginForm()
    return HttpResponseRedirect('dashboard')
    #return HttpResponseRedirect('dashboard')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login')

'''