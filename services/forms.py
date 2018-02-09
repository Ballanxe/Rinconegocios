from django import forms 
from django.utils.translation import ugettext_lazy as _ 

from .models import Services



class ServicesCreateForm(forms.ModelForm):


	class Meta:
		model = Services
		fields = [

			'name',
			'en_name',
			'serv_desc_es',
			'auto_trans',
			'category', 
			'serv_image',
			'discount',
			'price',
			'old_price',
			'meta_keywords',
			'meta_description',
			'meta_author',
			'meta_copyright',

		]

		widgets = {
			'serv_image': forms.FileInput,

		}

class ServicesUpdateForm(forms.ModelForm):


	class Meta:
		model = Services
		fields = [

			'name',
			'en_name',
			'serv_desc_es',
			'serv_desc_en',
			'auto_trans',
			'category', 
			'serv_image',
			'discount',
			'price',
			'old_price',
			'meta_keywords',
			'meta_description',
			'meta_author',
			'meta_copyright',

		]

		widgets = {
			'serv_image': forms.FileInput,

		}