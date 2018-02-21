"""project_7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^$', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

    



#project instructions



# need to give them a personal profile page where they share their first name, last name, email, date of birth, confirm email, short bio, upload avatar. 
# Their profile page is only visible to that person logged in. 

# Need to give them a bio page with their full bio. 

# Add a route to edit the profile. 

# need a 'profile' view, 'change_password' view with the url route '/profile/change_password' and use User.set_password() and then User.save(), 
# and an 'edit' view with the route '/profile/edit'.

# The email, date of birth, and biography will need validation (I'm assuming put it on the model as a validator. Ex: min_word = 1)
# Date of birth validation should accept three date formats: YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY.
# Email validation should check if emails match and are in valid format. 
# Bio validation should check that the bio is 10 characters or longer and properly escapes HTML formatting.

# Create a change password page. Page will ask for current password, new password, and confirm password.
# Set up validation to check that the current password is valid, that the new and confirm passwords match, and that the new password
    # follows the following policy: 
# check that old password is correct using 'User.check_password().'

#extra credit: 
# 1) Add additional form fields such as city/state/country, favorite animal/hobby. 
# Javascript utilized for date dropdown for date of birth feature.
# Javascript utilized for text formatting for the Bio feature.
# add an online image editor to the avatar. Rotate, crop, flip. 
# password strength meter is displayed when entering new passwords. 

#**************on edit profile page I need a 'confirm_email' field to make sure it matches, 
#***************for password change do User.set_password(), User.save(), User.check_password()