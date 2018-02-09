from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import FormView, ListView, TemplateView
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import ServiceDealForm

from services.models import Services
from companies.models import Affiliates
from .models import ServiceDeals

# Create your views here.


class ServiceDealView(FormView):

	form_class = ServiceDealForm
	template_name = 'service_deal_form_big.html'

	def form_valid(self, form):

		instance = form.save(commit=False)

		instance.buyer = self.request.user

		instance.service = get_object_or_404(Services, Q(slug__iexact=self.kwargs['slug']) | Q(slug_en__iexact=self.kwargs['slug']))

		instance.seller = instance.service.offerer

		instance.save()

		return HttpResponseRedirect(reverse('deals:thanks'))


	def get_context_data(self, *args, **kwargs):
		context = super(ServiceDealView, self).get_context_data(*args, **kwargs)

		context['object'] = get_object_or_404(Services, Q(slug__iexact=self.kwargs['slug']) | Q(slug_en__iexact=self.kwargs['slug']))

		print(context)

		return context


class AffiliateDealView(FormView):

	form_class = ServiceDealForm
	template_name = 'affiliate_deal_form_big.html'

	def form_valid(self, form):

		instance = form.save(commit=False)

		instance.buyer = self.request.user

		instance.seller = Affiliates.objects.get(slug__iexact=self.kwargs['slug'])

		instance.save()

		return HttpResponseRedirect(reverse('deals:thanks'))


	def get_context_data(self, *args, **kwargs):
		context = super(AffiliateDealView, self).get_context_data(*args, **kwargs)

		context['object'] = get_object_or_404(Affiliates, slug__iexact=self.kwargs['slug'])

		return context



class ServiceDealSellerListView(ListView):

	template_name = "seller_deal_list.html"

	def get_queryset(self):

		user_affiliates = [affiliate.id for affiliate in Affiliates.objects.filter(owner=self.request.user)]

		return ServiceDeals.objects.filter(seller__in=user_affiliates).order_by('-created')


class ServiceDealBuyerListView(ListView):

	template_name = "buyers_deal_list.html"

	def get_queryset(self):

		return ServiceDeals.objects.filter(buyer=self.request.user).order_by('-created')


class ThanksPageListView(TemplateView):

	template_name = "thanks_page.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ThanksPageListView, self).get_context_data(*args, **kwargs)

		context['object'] = ServiceDeals.objects.filter(buyer=self.request.user).latest('created')

		return context

