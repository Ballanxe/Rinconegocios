from django import forms 
from django.utils.translation import ugettext_lazy as _ 

from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import ServiceDeals
from accounts.models import User 


class ServiceDealForm(forms.ModelForm):


	class Meta:
		model = ServiceDeals
		fields = [

			'name',
			'last_name',
			'phone',
			'email',
			'message',


		]

		widgets = {

			'phone': PhoneNumberPrefixWidget(),

		}


