from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.shortcuts import render

from languages.fields import LanguageField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# from djangodeletes.softdeletes import SoftDeletable, SoftDeleteManager, SoftDeleteQuerySet 

from authtools.models import AbstractNamedUser
# Create your models here.

class User(AbstractNamedUser):

	phone = PhoneNumberField(null=True, blank=True)
	first_name = models.CharField(_('First name'), max_length=50, null=True, default=None, blank=True )
	last_name = models.CharField(_('Last name'), max_length=50, null=True, default=None, blank=True )
	language = LanguageField(_('Prefered language'), default=None, blank=True, null=True)
	country = CountryField(_('Country'), default=None, blank=True, null=True)


	# objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()

	def __str__(self):
		return self.email

	def get_absolute_url(self):

		return reverse('profiles:detail', kwargs={'pk':self.id})


	def check_user(self): 


		if (self.first_name == None) or (self.last_name == None) or (self.phone == ''): 

			return True 



