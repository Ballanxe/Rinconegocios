from django.conf.urls import url
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from .views import AffiliatesCreateView, AffiliatesListView, AffiliatesUpdateView, AffiliatesDetailView, AffiliatesDeleteView, AffiliatesDeletedList, AffiliatesPublicListView


# urlpatterns = [

# 	 # url(r'^en/affiliates/$', TemplateView.as_view(template_name='en/en_affiliates.html'), name="affiliates"),

# 	 # url(r'^es/afiliados/$', TemplateView.as_view(template_name='es/es_afiliados.html'), name="afiliados"),

# 	url(_(r'^$'), AffiliatesPublicListView.as_view(), name="list"),
#     url(_(r'^create/$'), AffiliatesCreateView.as_view(), name="create"),
#     url(_(r'^companies/$'), AffiliatesListView.as_view(), name="my_list"),
#     url(_(r'^update/(?P<slug>[\w-]+)/$'), AffiliatesUpdateView.as_view(), name="update"),
#     url(_(r'^(?P<slug>[\w-]+)/$'), AffiliatesDetailView.as_view(), name="detail"),
#     url(_(r'^delete/(?P<pk>\d+)/$'), AffiliatesDeleteView.as_view(), name="delete"),
#     url(_(r'^delete/list/$'), AffiliatesDeletedList.as_view(), name="delete_list"),

# ]

