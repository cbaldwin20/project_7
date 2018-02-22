from django import forms 
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import (validate_password,
 password_validators_help_texts, get_default_password_validators)
import re

from froala_editor.widgets import FroalaEditor


#class DateInput(forms.DateInput):
    #input_type = 'date'

class EditForm(forms.ModelForm):
    """Edits the profile information"""

    #bio = forms.CharField(min_length=10, widget=forms.Textarea)
    bio = forms.CharField(min_length=10, widget=FroalaEditor)
    verify_email = forms.EmailField(label="Please verify your \
        email address")
    
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',
            'birthday', 'city', 'state', 'country', 'favorite_animal',
             'hobby', 'email', 'verify_email', 'bio','image')
        # for my jquery ui calendar picker. 
        widgets = {'birthday': forms.DateInput(attrs={'class': \
            'datepicker'})}

    class Media:
    	css = {'all': ('css/jquery-ui.min.css',),
    			'all': ('css/jquery-ui.structure.min.css',),
    			'all': ('css/jquery-ui.theme.min.css',),
    	}
    	js = ('js/jquery-ui-1.12.1.custom/jquery-ui.min.js',)

    def clean(self):
        """checks to see if email and confirm match"""
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields")

        #birthday = cleaned_data.get('birthday')
		
        #if not re.search(r'^\d\d\d\d[-]\d\d[-]\d\d$', birthday):
        	#if not re.search(r'^\d\d[/]\d\d[/]\d\d\d\d$', birthday):
        		#if not re.search(r'^\d\d[/]\d\d[/]\d\d$', birthday):
        			#raise forms.ValidationError(
                #"You need to enter the birthday correctly")


class ChangePasswordForm(forms.Form):
    """changes password"""

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    current_password = forms.CharField(max_length=32, 
        widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    verify_new_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        """checks to see if new and confirm passwords match"""
        
        new_password = self.cleaned_data.get('new_password')
        verify = self.cleaned_data.get('verify_new_password')
        
        if new_password != verify:
            raise forms.ValidationError(
                "The new passwords did not match")

        user = self.request.user.the_profile
        first_name = user.first_name.lower()
        last_name = user.last_name.lower()
        username = self.request.user.username.lower()

        if (first_name in new_password.lower() or last_name in
          new_password.lower() or username in new_password.lower()):
            raise forms.ValidationError("The new password cannot contain "
                "parts of your full name ({} {}) or username ({}).".format(
                user.first_name, user.last_name, self.request.user.username))

        # I created a custom validator 'NoUsername' for registering
        # but don't want it for my change password form. 
        validators = get_default_password_validators()
        validators = validators[:-1]
        validate_password(new_password, password_validators=validators)
        


        