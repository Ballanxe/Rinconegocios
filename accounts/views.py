from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import UpdateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from .models import User
from .forms import UserUpdateInformation
# Create your views here.


class ProfileDetailView(UpdateView):
	template_name = 'profiles/dashboard_profile.html'
	form_class = UserUpdateInformation

	def form_valid(self, form):
		
		form.save()
		messages.success(self.request, _('Your data has been updated'))
		return HttpResponseRedirect(reverse('affiliates:my_list'))

	def get_object(self):
		pk = self.kwargs.get("pk")
		email = self.request.user.email

		if email is None:
			raise Http404
		return get_object_or_404(User, id__iexact=pk, email__iexact=email, is_active=True)


