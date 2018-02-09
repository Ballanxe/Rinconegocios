from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, ListView, FormView, UpdateView, DeleteView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _ 
from django.http import HttpResponseRedirect
from django.utils.html import escape, strip_tags
from django.db.models import Q
from django.utils import translation

from authtools.views import LoginView, PasswordResetView
from googletrans import Translator
from .forms import ServicesCreateForm, ServicesUpdateForm
from companies.models import Affiliates
from .models import Services
# Create your views here.


class ServicesCreateView(LoginRequiredMixin, FormView):

	template_name="service_create.html"
	form_class= ServicesCreateForm
	translator = Translator()


	def form_valid(self, form):

		instance = form.save(commit=False)

		instance.offerer = Affiliates.objects.get(slug__iexact=self.kwargs['slug'])

		if instance.auto_trans:

			translated = self.translator.translate(strip_tags(instance.serv_desc_es), dest='en')

			instance.serv_desc_en = translated.text.replace("& nbsp; $ Nbsp;", " ")


		name = instance.name 

		instance.save()


		messages.success(self.request, _(f'The service \"{name}\" has been created'))

		return HttpResponseRedirect(reverse('services:my_list'))



	def get_context_data(self, *args, **kwargs):
		context = super(ServicesCreateView, self).get_context_data(*args, **kwargs)

		context['object'] = Affiliates.objects.get(slug__iexact=self.kwargs['slug'])

		return context

	# def get_form_kwargs(self):
	# 	kwargs = super(ServicesCreateView, self).get_form_kwargs()
	# 	kwargs['slug'] = self.request.GET.get('slug')
	# 	print(kwargs)
	# 	return kwargs

class ServicesListView(LoginRequiredMixin, ListView):

	template_name="my_services_list.html"

	def get_queryset(self):

		# a = Services.objects.filter(offerer__owner=self.request.user.id)
		a = Services.objects.all()
		return a

	def get_context_data(self, *args, **kwargs):

		context = super(ServicesListView, self).get_context_data(*args, **kwargs)

		context['objects'] = Services.objects.filter(offerer__owner=self.request.user.id)

		return context


class ServicesUpdateView(LoginRequiredMixin, UpdateView):

	template_name="service_update.html"
	form_class = ServicesUpdateForm
	translator = Translator()


	def form_valid(self, form):

		instance = form.save(commit=False)


		if instance.auto_trans:


			translated = self.translator.translate(strip_tags(instance.serv_desc_es), dest='en')

			instance.serv_desc_en = translated.text.replace("& nbsp;", " ").replace("& Nbsp;", " ")

			instance.save()

			messages.success(self.request, _(f'The service has been updated'))

			messages.info(self.request, _(f'The service description has been translated. Remember edit it.'))

			return HttpResponseRedirect(self.request.path) 


		instance.save()

		messages.success(self.request, _(f'The service has been updated'))

		return HttpResponseRedirect(reverse('services:my_list'))

	def get_initial(self):
		"""
		Returns the initial data to use for forms on this view.
		"""
		initial = super(ServicesUpdateView, self).get_initial()

		initial['auto_trans'] = False


		return initial


	def get_object(self):

		slug = self.kwargs.get("slug")

		if slug is None:

			raise Http404
			
		return get_object_or_404(Services, Q(slug__iexact=slug) | Q(slug_en__iexact=slug))


class ServicesDetailView(DetailView):

	template_name = "services_detail.html"

	def get_object(self):

		slug = self.kwargs.get("slug")

		if slug is None:

			raise Http404
			
		return get_object_or_404(Services, Q(slug__iexact=slug) | Q(slug_en__iexact=slug))

	def get_context_data(self,*args, **kwargs):

		context = super(ServicesDetailView, self).get_context_data(*args, **kwargs)

		context['n_publications'] =  Services.objects.filter(offerer__owner=self.request.user.id).count()

		return context 


class ServicesDeleteView(DeleteView):

	model=Services
	template_name='services_confirm_delete.html'
	success_url='services:my_list'

	def delete(self, request, *args, **kwargs):

		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()

		messages.success(self.request, _(f'The service has been deleted'))
		return HttpResponseRedirect(success_url)

	def get_success_url(self):

		return reverse(self.success_url)


class ServicesDeletedList(ListView):

	template_name="services_deleted_list.html"

	def get_queryset(self):
		return Services.objects.only_deleted()



class ServicesPublicListView(ListView):

	template_name="services_public_list.html"

	def get_queryset(self):
		query = self.request.GET.get('q')
		if not query: 

			return Services.objects.all().order_by('-created')


	def get_context_data(self, *args, **kwargs):
		context = super(ServicesPublicListView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		query = str(query).strip()
		# qs = Services.objects.all().search(query).order_by('-created') # Aqui estoy activando el query manager 
		qs = Services.objects.filter(

	            Q(name__icontains=query)|
	            Q(name__iexact=query)|
	            Q(category__icontains=query)|
	            Q(category__iexact=query)

	        ).distinct()

		if qs.exists():

			context['search'] = qs
		else:
			# context['no_results'] = _('No results for your search')
			context['search'] = 0 

		return context


	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ServicesPublicListView, self).get_context_data(*args, **kwargs)
	# 	query = self.request.GET.get('q')
	# 	qs = Affiliates.objects.all().search(query).order_by('-created')#Aqui estoy activando el query manager 
	# 	if qs.exists():
	# 		context['search'] = qs

	# 	return context



# class MainView(TemplateView):

# 	template_name = 'index.html'




