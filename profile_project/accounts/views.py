from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import (AuthenticationForm, 
                                            UserCreationForm)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import (
                                    password_validators_help_texts)
#import re
import datetime


from accounts.forms import EditForm, ChangePasswordForm 


def sign_in(request):
    """signs person in"""
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        #redirects to profile
                        # instead of homepage
                        reverse('accounts:profile') 
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    """register page"""
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            # I changed this 'HttpResponseRedirect' from 'home' to 
            #'accounts:edit'. 
            return HttpResponseRedirect(reverse(
                            'accounts:create_profile'))  
    return render(request, 'accounts/sign_up.html', {'form': form})

@login_required
def sign_out(request):
    """sings person out"""
    logout(request)
    messages.success(request, 
            "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))

#def time_converter(birthday):
    #if re.search(r'\d\d\d\d[-]\d\d[-]\d\d', birthday):
       # final_bday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    #elif re.search(r'\d\d[/]\d\d[/]\d\d\d\d', birthday):
        #final_bday = datetime.datetime.strptime(birthday, '%m/%d/%Y')
    #elif re.search(r'\d\d[/]\d\d[/]\d\d', birthday):
       # final_bday = datetime.datetime.strptime(birthday, '%m/%d/%y')
    #else:
        #final_bday = 0
    #return final_bday

@login_required
def create_profile(request):
    """user fills out profile"""
    if request.method == 'POST':
        form = EditForm(request.POST, files=request.FILES)
        if form.is_valid(): 
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            #birthday = new_profile.cleaned_data['birthday']
            #birthday = time_converter(birthday)
            #new_profile.birthday = birthday  
            new_profile.save()
            messages.success(request, "Profile created!")
            return redirect('accounts:profile')
    else:
        form = EditForm()
    a = "a"
    return render(request, 'accounts/edit_profile.html', 
                                        {'form': form, "a": a })


@login_required
def edit_profile(request):
    """user can edit profile"""
    if request.method == 'POST':
        user = request.user.the_profile 
        form = EditForm(request.POST, files=request.FILES, 
                                                    instance=user)
        if form.is_valid():
            #birthday = form.cleaned_data['birthday']
            #birthday = time_converter(birthday)
            #form.birthday = birthday  
            form.save()
            messages.success(request, "Profile updated!")
            return redirect('accounts:profile')
    else:
        user = request.user.the_profile 
        form = EditForm(instance=user)
        form.fields["verify_email"].initial = user.email
        #init_birthday = user.birthday.strftime('%m/%d/%Y')
        #print(type(init_birthday))
        #form.fields["birthday"].initial = init_birthday
        
    return render(request, 'accounts/edit_profile.html', 
                                                    {'form': form})


@login_required
def profile(request):
    """shows user's profile page"""
    user_profile = request.user.the_profile
    return render(request, 'accounts/profile.html', 
                                    { 'user_profile': user_profile })



@login_required
def bio(request):
    """shows users bio page"""
    user_profile = request.user.the_profile
    return render(request, 'accounts/bio_page.html', 
                                    { 'user_profile': user_profile })


@login_required
def change_password(request):
    """page to change password"""
    help_texts = password_validators_help_texts(
                                            password_validators=None)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
        
            if request.user.check_password(current_password):
                new_password = form.cleaned_data.get('new_password')
                user = request.user 
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password updated!")
                return redirect('accounts:profile')
            else:
                messages.error(request, "The password did not match \
                    your current password!")
                return redirect('accounts:change_password')
    else:
        form = ChangePasswordForm()       
    return render(request, 'accounts/change_password.html', 
                        {'form':form, 'help_texts': help_texts })


