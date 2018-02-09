from django import forms 
from django.utils.translation import ugettext_lazy as _ 
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Affiliates


class AffiliatesCreateForm(forms.ModelForm):

	# email 				= forms.EmailField()
	# category				= forms.CharField(required=False, validators=[validate_category])

	class Meta:
		model = Affiliates
		fields = [

			'name',
			'email',
			'phone',
			'category', 
			'logo',
			'lead_magnet',
			'description_es',
			'auto_trans',
			'meta_keywords',
			'meta_description',
			'meta_author',
			'meta_copyright',


		]
		widgets = {
			'logo': forms.FileInput,
			'phone': PhoneNumberPrefixWidget(),
		}



class AffiliatesTraslatedUpdateForm(forms.ModelForm):

	# email 				= forms.EmailField()
	# category				= forms.CharField(required=False, validators=[validate_category])

	class Meta:
		model = Affiliates
		fields = [

			'name',
			'email',
			'phone',
			'category', 
			'logo',
			'lead_magnet',
			'description_es',
			'auto_trans',
			'description_en',
			'meta_keywords',
			'meta_description',
			'meta_author',
			'meta_copyright',


		]

		widgets = {
			'logo': forms.FileInput,
			'phone': PhoneNumberPrefixWidget(),
		}



# class AffiliatesTranslateForm(forms.ModelForm): 

# 	class Meta:
# 		model=Affiliates
# 		fields=[

# 			'description_es',
# 			'description_en',

# 		]