from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages 
from django.http import HttpResponseRedirect, Http404
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView, DeleteView
from django.utils.html import escape, strip_tags
from django.db.models import Q

from googletrans import Translator

from .forms import AffiliatesCreateForm, AffiliatesTraslatedUpdateForm
from django.utils.translation import ugettext_lazy as _

from .models import Affiliates

# Create your views here.

class AffiliatesCreateView(LoginRequiredMixin, CreateView):

	template_name='dashboard_affiliates.html'
	form_class= AffiliatesCreateForm
	translator = Translator()


	def form_valid(self, form):

		instance = form.save(commit=False)

		instance.owner = self.request.user

		if instance.auto_trans:

			translated = self.translator.translate(strip_tags(instance.description_es), dest='en')

			instance.description_en = translated.text.replace("& nbsp;", " ")

		name = instance.name 

		instance.save()

		messages.success(self.request, _(f'The company \"{name}\" has been created'))

		return HttpResponseRedirect(reverse('affiliates:my_list'))


class AffiliatesListView(LoginRequiredMixin, ListView):

	template_name="my_affiliates_dashboard.html"

	def get_queryset(self):
		return Affiliates.objects.filter(owner=self.request.user).order_by('-created')




class AffiliatesPublicListView(ListView):

	template_name="en/affiliates.html"

	def get_queryset(self):

		query = self.request.GET.get('q')
		if not query: 

			return Affiliates.objects.all().order_by('-created')


	def get_context_data(self, *args, **kwargs):
		context = super(AffiliatesPublicListView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		query = str(query).strip()
		qs = Affiliates.objects.filter(

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



class AffiliatesUpdateView(LoginRequiredMixin, UpdateView):

	template_name="affiliates_update.html"
	form_class= AffiliatesTraslatedUpdateForm

	translator = Translator()


	def form_valid(self, form):

		instance = form.save(commit=False)

		name = instance.name

		if instance.auto_trans:


			translated = self.translator.translate(strip_tags(instance.description_es), dest='en')

			instance.description_en = translated.text.replace("& nbsp;", " ")

			instance.save()

			messages.success(self.request, _(f'The company \"{name}\" has been updated'))

			messages.info(self.request, _(f'The description has been translated. Remember edit it.'))

			return HttpResponseRedirect(self.request.path) 


		instance.save()

		messages.success(self.request, _(f'The company \"{name}\" has been updated'))

		return HttpResponseRedirect(reverse('affiliates:my_list'))
		# return HttpResponseRedirect(self.request.path)

	def get_initial(self):
		"""
		Returns the initial data to use for forms on this view.
		"""
		initial = super(AffiliatesUpdateView, self).get_initial()

		initial['auto_trans'] = False


		return initial


	# def get_context_data(self, *args, **kwargs):

	# 	context = super(AffiliatesUpdateView, self).get_context_data(*args, **kwargs)

	# 	name = self.get_object().name

	# 	context['title'] = f'Update Restaurant: {name}'

	# 	if self.get_object().auto_trans == True:

	# 		self.get_object().auto_trans = False

	# 	return context 

	def get_queryset(self):

		slug = self.kwargs.get("slug")

		qs = Affiliates.objects.filter(owner=self.request.user, slug=slug)


		return qs



class AffiliatesDetailView(DetailView):

	template_name = "affiliates_detail.html"

	def get_object(self):

		slug = self.kwargs.get("slug")

		if slug is None:

			raise Http404
			
		return get_object_or_404(Affiliates, slug__iexact=slug)

	def get_context_data(self, *args, **kwargs):

		context = super(AffiliatesDetailView, self).get_context_data(*args, **kwargs)

		slug = self.kwargs.get("slug")

		obj = get_object_or_404(Affiliates, slug__iexact=slug)

		context['available_offers']	= obj.services_set.all()

		return context



class AffiliatesDeleteView(DeleteView):
	model=Affiliates
	template_name='confirm_delete.html'
	success_url='affiliates:my_list'

	def delete(self, request, *args, **kwargs):

		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()

		messages.success(self.request, _(f'The company has been deleted'))
		return HttpResponseRedirect(success_url)

	def get_success_url(self):

		return reverse(self.success_url)


class AffiliatesDeletedList(ListView):

	template_name="affiliates_deleted_list.html"

	def get_queryset(self):
		return Affiliates.objects.only_deleted()


class AffiliatesTranslateView(UpdateView):

	template_name = "affiliates_translate.html"
	form_class = ""



# def affiliates_update(request, slug, template_name="affiliates_update.html"):

#     affiliates = get_object_or_404(Affiliates, slug=slug)
#     form = AffiliatesTraslatedUpdateForm(request.POST or None, request.FILES or None, instance=affiliates)
#     translate_form = AffiliatesTranslateForm(request.POST or None, instance=affiliates)
#     translator = Translator()

#     if form.is_valid():

#         form.save()
#         return HttpResponseRedirect(request.path)

#     if translate_form.is_valid():

#   #   	translated = translator.translate(instance.description_es, dest='en')

# 		# instance.description_en = translated.text 

#     	form.save()
#     	return HttpResponseRedirect(request.path)

#     return render(request, template_name, {'form':form, 'translate_form': translate_form, 'object':affiliates})