from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import escape
# from django.utils.timezone import now as timezone_now
from django.utils import timezone
from django.utils.safestring import mark_safe

class CreationModificationDateMixin(models.Model):
	"""
	Abstract base class with a creation and modification date and time	

	"""

	created = models.DateTimeField(
		_("creation date and time"),
		editable=False,
		# auto_now_add=True,
		null=True,

	)

	modified = models.DateTimeField(
		_("modification date and time"),
		null=True,
		# editable=True,
		# # auto_now=True,
	)

	def save(self, *args, **kwargs):

		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(CreationModificationDateMixin, self).save(*args, **kwargs)


	# def save_it(self, *args, **kwargs):
	# 	'''
	# 	You can substitute this method by auto_add and auto_add_now model settings.
	# 	'''
	# 	if not self.pk:
	# 		self.created = timezone_now()

	# 	if not self.created:
	# 		self.created = timezone_now()
	# 		self.modified = timezone_now()
	# 		super(CreationModificationDateMixin, self).save(*args, **kwargs)
	# 	save.alters_data = True

	class Meta:

		abstract = True



class MetaTagsMixin(models.Model):
	'''
	Abstract base class for meta tags in the <head> section
	'''

	meta_keywords = models.CharField(
		_("SEO Keywords"),
		max_length=255,
		blank=True,
		help_text=_("Separate keywords by comma."),
	)

	meta_description = models.CharField(
		_("SEO Description"),
		max_length=255,
		blank=True,
	)

	meta_author = models.CharField(
		_("SEO Author"),
		max_length=255,
		blank=True,
	)

	meta_copyright = models.CharField(
		_("SEO Copyright"),
		max_length=255,
		blank=True,
	)

	class Meta:
		abstract=True

	def get_meta_keywords(self):
		tag = ""
		if self.meta_keywords:
			tag = '<meta name="keywords" content="%s" />\n' %\
				escape(self.meta_keywords)
		return mark_safe(tag)

	def get_meta_description(self):
		tag = ""
		if self.meta_description:
			tag = '<meta name="description" content="%s" />\n' %\
				escape(self.meta_description)
		return mark_safe(tag)

	def get_meta_author(self):
		tag = ""
		if self.meta_author:
			tag = '<meta name="author" content="%s" />\n' %\
				escape(self.meta_author)
		return mark_safe(tag)

	def get_meta_copyright(self):
		tag = ""
		if self.meta_copyright:
			tag = '<meta name="copyright" content="%s" />\n' %\
				escape(self.meta_copyright)
		return mark_safe(tag)

	def get_meta_tags(self):
		return mark_safe("".join((
			self.get_meta_keywords(),
			self.get_meta_description(),
			self.get_meta_author(),
			self.get_meta_copyright(),
		)))


class ServiceDealMixin(models.Model):


	buyer_comment = models.TextField(_('Buyer Comment'), null=True, blank=True, help_text=_('Tell us what was your experience with this service?'))

	seller_comment = models.TextField(_('Seller Comment'), null=True, blank=True, help_text=_('What do you want to say about this client?'))

	buy_is_finished = models.BooleanField(_("Buyer tells deal is finished"), default=False, help_text=_("Did you buy this service ?"))

	sell_is_finished = models.BooleanField(_("Seller tells deal is finished"), default=False, help_text=_("Did you sell this service ?"))

	buyer_is_contacted = models.BooleanField(_("Buyer tells has been contated"), default=False, help_text=_("Did the company make contact with you ?"))

	seller_has_contacted = models.BooleanField(_("Seller tells has contacted buyer"), default=False, help_text=_("Have you already made contact with this client ?"))

	is_closed = models.BooleanField(_("This means that de deal was successful"), default=False)


	class Meta:
		abstract=True


	def get_contacted_deal(self):

		if self.buyer_is_contacted and self.seller_has_contacted:
			return True 


	def get_finished_deal(self):

		if self.buy_is_finished and self.sell_is_finished:
			
			self.is_closed = True 

			return True 

	def get_closed_deal(self):

		if self.is_closed:

			return True 		