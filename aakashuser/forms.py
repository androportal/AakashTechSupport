# FORMS
import datetime
from django.core.validators import RegexValidator

__author__ = 'ushubham27'

from django import forms
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from aakashuser.models import Post, Category, UserProfile
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import *

class UserForm(forms.ModelForm):
    username = forms.CharField(
        min_length=6,
        max_length=30,
        required=True,
        error_messages={
            'required': 'Username is required.'
        },
        validators=[
            RegexValidator('^[a-zA-Z0-9]*$', message='Username must be Alphanumeric'),
        ],
        label='Username',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username to login*.'}),
        )

    first_name = forms.CharField(
        min_length=2,
        max_length=20,
        required=True,
        error_messages={
            'required': 'First name is required.'
        },
        validators=[
            RegexValidator('^[a-zA-Z]*$', message='First name must be Albhates'),
        ],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Coordinator first name*.'}),
        )

    last_name = forms.CharField(
        min_length=2,
        max_length=20,
        required=True,
        error_messages={
            'required': 'Last name is required.'
        },
        validators=[
            RegexValidator('^[a-zA-Z]*$', message='Last name must be Alphabates'),
        ],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Coordinator last name*.'}),
        )

    email = forms.CharField(
        max_length=30,
        required=True,
        error_messages={
            'required': 'Valid Email address is required.'
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Coordinator valid email*.'}),
        )

    password = forms.CharField(
        min_length=6,
        max_length=16,
        required=True,
        error_messages={
            'required': 'Password is missing.'
        },
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Coordinator password*.'}),

        )

	# add DOB field and highets qualification and gender working as 
    password1 = forms.CharField(
        min_length=6,
        max_length=16,
        required=True,
        error_messages={
            'required': 'reenter correct password.'
        },
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Re-enter password'}),
        )
        
    netbook_serial_no = forms.CharField(
    	max_length=20,
    	required=True,
    	error_messages={
            'required': 'Please enter netbook number'
        },
        validators=[
            RegexValidator('^[a-zA-Z0-9]*$', message='netbook number should be numeric'),
        ],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'please enter netbook number'}),
        )
    	 
    #dob = models.DateField(auto_now_add=False, default=Date)
    netbook_serial_no = forms.CharField(
    	max_length=20,
    	required=True,
    	error_messages={
            'required': 'Please enter netbook number'
        },
        validators=[
            RegexValidator('^[a-zA-Z0-9]*$', message='netbook number should be numeric'),
        ],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'please enter netbook number'}),
        )
    	 
    	 
    
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password1','netbook_serial_no')

"""
class PostForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        help_text="",
        required=True,
        error_messages={'required:' 'Renter the question tile.'}
    )
    body = forms.Textarea(
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
            }
        ),
        help_text="",
        required=True,
        error_messages={
            'required': 'Re-enter the text.'
        }
    )

    tags = forms.ChoiceField(
        choices=[(x['category'], str(x['category']))
                 for x in Category.objects.values('category')],
        help_text="please select the category of your problem"
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

    def clean_created_date_time(self):
        return datetime.datetime.now()

"""

class UserProfileForm(forms.ModelForm):

    location = forms.CharField(
			    max_length=30,
			    error_messages={
			    'required': 'location is required.'
			    },
			    #help_text="Enter your location:",
			    label="Location",
			    required=True,
			    widget=forms.TextInput(
				    attrs={'class': 'form-control', 'placeholder': 'Location'}),
			    )
			    
    skills = forms.CharField(
			    max_length=100,
			    required=True,
			    error_messages={
			    'required': 'skills is required.'
			    },
			    #help_text="Enter your skills:",
			    widget=forms.TextInput(
				    attrs={'class': 'form-control', 'placeholder': 'Skills'}),
			    )
			    
    avatar = forms.ImageField(
			    label='Profile picture',
			    help_text='png file of size less than 1MB required.',
			    required=False,
			    widget=forms.FileInput(attrs={
			     'placeholder': 'Profile picture.'}),
				)
			      

	

    
    class Meta:
        model = UserProfile
        fields = ('location', 'skills','avatar')
        
        
