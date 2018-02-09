import os
import datetime
from django.db import models
from enum import Enum
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.utils.timezone import now as timezone_now
from django.utils import translation
from django.db.models import Q

from djangodeletes.softdeletes import SoftDeletable, SoftDeleteManager, SoftDeleteQuerySet 
from djangodeletes.softdeletes.mixins import SoftDeleteQuerySetMixin, SoftDeleteManagerMixin
from tinymce import HTMLField
from googletrans import Translator

from companies.validators import file_size
from utils.models import CreationModificationDateMixin, MetaTagsMixin
from utils.slugy import unique_slug_generator, english_unique_slug_generator
from companies.models import Affiliates
from accounts.models import User

# Create your models here.

def upload_to(instance, filename):
	now = timezone_now()
	filename_base, filename_ext = os.path.splitext(filename)
	return "media/%s%s" % (
		now.strftime("%Y/%m/%Y%m%d%H%M%S"),
		filename_ext.lower(),
	)

def upload_file_to(instance, filename):
	now = timezone_now()
	filename_base, filename_ext = os.path.splitext(filename)
	return "media/documents/%s%s" % (
		now.strftime("%Y/%m/%Y%m%d%H%M%S"),
		filename_ext.lower(),
	)





class Services(SoftDeletable, CreationModificationDateMixin, MetaTagsMixin):

	class CATEGORIES(Enum):

		marketing			= ('marketing', _('Marketing'))
		finance				= ('finance', _('Finance'))
		development			= ('development', _('Development'))
		vacations 			= ('vacations', _('Vacations'))
		design 				= ('design', _('Design'))
		information_security= ('information_security', _('Information Security'))

		@classmethod
		def get_value(cls, member):
			return cls[member].value[0]


	offerer = models.ForeignKey(Affiliates, on_delete=models.CASCADE)
	name = models.CharField( _('Title'), max_length=50, null=False, default=None, blank=False)
	en_name = models.CharField( _('English Title'), max_length=50, null=True, default=" ", blank=True)
	serv_desc_es = HTMLField(_("Spanish Service Description"),null=True, blank=True)
	serv_desc_en  = HTMLField(_("English Service Description"),null=True, blank=True)
	category = models.CharField(
		max_length=25,
		choices=[x.value for x in CATEGORIES]
	)

	serv_image = models.ImageField(_('Service Image'), upload_to =upload_to, blank=True, null=True, validators=[file_size])
	price = models.PositiveSmallIntegerField(_('Price'), null=True, blank=True)
	old_price = models.PositiveSmallIntegerField(_('Price Before'), null=True, blank=True)
	discount = models.PositiveSmallIntegerField(_('Discount'), null=True, blank=True)
	prospects = models.PositiveSmallIntegerField(_('Interested People'), null=True, blank=True)
	clients = models.PositiveSmallIntegerField(_('Satisfied Clients'), null=True, blank=True)
	days_left = models.PositiveSmallIntegerField(_('Days left'), null=True, blank=True)
	is_active = models.BooleanField(_("Active "), default=True, help_text=_('This tells if a services is published or not'))

	auto_trans = models.BooleanField(_("Automatic Translation"), default=False, help_text=_('Create automatic translation of description. You can edit it later in update page'))

	slug = models.SlugField(max_length=255, null=True, blank=True)

	slug_en = models.SlugField(max_length=255, null=True, blank=True)

	objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()


	def __str__(self):
		return self.name


	def get_service_lang(self):

		 current = translation.get_language()

		 text = _('English description isn\'t available')

		 if self.serv_desc_en == "": 
		 	return text

		 if current == 'en':
		 	return self.serv_desc_en
		 elif current ==  'es':
		 	return self.serv_desc_es


	def get_service_name(self):

		current = translation.get_language()
		translator = Translator()

		if not self.en_name and (current == 'en'):

			name_translated = translator.translate(self.name, dest='en')

			return name_translated.text

		elif self.en_name and (current == 'en'):

			return self.en_name


		elif current == 'es':

			return self.name


	def get_days_left(self):

		created =  self.created 

		ended = created + datetime.timedelta(days=30)

		return (ended - created).days


	def get_lang_slug(self):

		current = translation.get_language()

		if self.slug_en == "":
			return self.slug

		elif (current == 'en'): 

			return self.slug_en

		elif (current == 'es'):

			return self.slug


def rl_pre_save_receiver(sender, instance, *args, **kwargs):

	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		instance.slug_en = english_unique_slug_generator(instance)	


pre_save.connect(rl_pre_save_receiver, sender=Services)