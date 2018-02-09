import os
from django.db import models
from enum import Enum
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now as timezone_now
from django.utils import translation
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from django.core.validators import FileExtensionValidator

from djangodeletes.softdeletes import SoftDeletable, SoftDeleteManager, SoftDeleteQuerySet 
from djangodeletes.softdeletes.mixins import SoftDeleteQuerySetMixin, SoftDeleteManagerMixin
from phonenumber_field.modelfields import PhoneNumberField
from utils.slugy import unique_slug_generator
from tinymce import HTMLField

from utils.models import CreationModificationDateMixin, MetaTagsMixin
from .validators import file_size
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


class AffiliatesQuerySet(SoftDeleteQuerySetMixin, models.query.QuerySet):

	'''Se agrego esta funcion a SoftDeleteQuerySetMixin'''


	# def search(self, query):

	# 	if query:
	# 		query = query.strip()
	# 		return self.filter(

	# 			Q(name__icontains=query)|
	# 			Q(name__iexact=query)|
	# 			Q(category__icontains=query)|
	# 			Q(category__iexact=query)

	# 		).distinct()
	# 	return self


class AffiliatesManager(SoftDeleteManagerMixin, models.Manager):
	queryset_class = SoftDeleteQuerySet



	def get_queryset(self):
		return AffiliatesQuerySet(self.model, using=self._db)

	def search(self, query):

		'''Ejecuta la busqueda'''

		return self.get_queryset().search(query) 
# category		= models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])


class Affiliates(SoftDeletable, CreationModificationDateMixin, MetaTagsMixin):

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

	owner =  models.ForeignKey(User, on_delete=models.CASCADE) 
	name = models.CharField( _('Name'), max_length=50, null=False, default=None, blank=False)
	email = models.EmailField(_('Corporative Email'), null=False, blank=False, default=None)
	
	phone = PhoneNumberField(default=None, blank=True, null=True)
	category = models.CharField(
		max_length=25,
		choices=[x.value for x in CATEGORIES]
	)
	logo = models.ImageField(_('Logo'), upload_to =upload_to, blank=True, null=True, validators=[file_size])
	lead_magnet = models.FileField(_('Lead Magnet'), upload_to=upload_file_to, blank=True, null=True, validators=[FileExtensionValidator(['pdf','png'])])	
	years = models.PositiveSmallIntegerField(_('Years of fundation'), null=True, blank=True)
	conversions = models.PositiveSmallIntegerField(_('Conversions'), null=True, blank=True)
	contracts = models.PositiveSmallIntegerField(_('Terminated contracts'), null=True, blank=True)
	prospects = models.ManyToManyField(User, related_name=_('Prospects'))
	description_en = HTMLField(_("English Description"),null=True, blank=True)
	description_es = HTMLField(_("Spanish Description"),null=False, blank=False)
	auto_trans = models.BooleanField(_("Automatic Translation"), default=False, help_text=_('Create automatic translation of description. You can edit it later in update page'))
	# services = models.ForeignKey()
	mission = models.TextField(_("Mission"),null=False, blank=False)
	vision = models.TextField(_("Vision"),null=False, blank=False)
	slug = models.SlugField(max_length=255, null=True, blank=True)

	objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()
	# objects = AffiliatesManager.from_queryset(AffiliatesQuerySet)()


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return f"/restaurants/{self.slug}"
		return reverse('affiliates:detail', kwargs={'slug':self.slug})


	def get_affiliate_lang(self):

		 current = translation.get_language()

		 text = _('English description isnt available')

		 if self.description_en == "": 
		 	return text

		 if current == 'en':
		 	return self.description_en
		 elif current ==  'es':
		 	return self.description_es



def rl_pre_save_receiver(sender, instance, *args, **kwargs):

	if not instance.slug:
		instance.slug = unique_slug_generator(instance)	



pre_save.connect(rl_pre_save_receiver, sender=Affiliates)

