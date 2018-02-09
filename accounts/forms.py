from django import forms 
from django.utils.translation import ugettext_lazy as _ 
from phonenumber_field.widgets import PhoneNumberPrefixWidget, PhonePrefixSelect

from .models import User


class UserUpdateInformation(forms.ModelForm):
	# email 				= forms.EmailField()
	# category				= forms.CharField(required=False, validators=[validate_category])
	class Meta:
		model = User
		fields = [

			'name',
			'email', 
			'phone',
			'first_name',
			'last_name',
			'language',
			'country',

		]

		widgets = {

			'phone': PhoneNumberPrefixWidget()

		}


		





