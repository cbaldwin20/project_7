from django import forms 
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import (validate_password,
 password_validators_help_texts)
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
    current_password = forms.CharField(max_length=32, 
        widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    verify_new_password = forms.CharField(widget=forms.PasswordInput)

    

    password_validators_help_texts(password_validators=None)

    def clean(self):
        """checks to see if new and confirm passwords match"""
        
        new_password = self.cleaned_data.get('new_password')
        verify = self.cleaned_data.get('verify_new_password')
        print(new_password)
        print(verify)
        if new_password != verify:
            raise forms.ValidationError(
                "The new passwords did not match")

        validate_password(new_password)
        


        