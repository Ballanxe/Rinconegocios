from django.db import models
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from djangodeletes.softdeletes import SoftDeletable, SoftDeleteManager, SoftDeleteQuerySet


from accounts.models import User
from services.models import Services
from companies.models import Affiliates
from utils.models import CreationModificationDateMixin, ServiceDealMixin
# Create your models here.


class ServiceDeals(SoftDeletable, CreationModificationDateMixin, ServiceDealMixin):


	service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)

	seller  =  models.ForeignKey(Affiliates, on_delete=models.CASCADE)

	buyer = models.ForeignKey(User, on_delete=models.CASCADE)

	name = models.CharField( _('Name'), max_length=50, null=False, default=None, blank=False) 

	last_name = models.CharField( _('Last Name'), max_length=50, null=False, default=None, blank=False)

	email  =  models.EmailField(_('Corporative Email'), null=False, blank=False, default=None)

	phone = PhoneNumberField(_('Phone Number'), null=True, blank=True)

	message = models.TextField(_('Message'), null=True, blank=True)

	objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()


	def __str__(self):
		return self.buyer.email