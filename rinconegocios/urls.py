from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.views.generic import TemplateView
# from services.views import MainView  

from companies.views import AffiliatesCreateView, AffiliatesListView, AffiliatesUpdateView, AffiliatesDetailView, AffiliatesDeleteView, AffiliatesDeletedList, AffiliatesPublicListView

from accounts.views import ProfileDetailView

from services.views import ServicesCreateView, ServicesListView, ServicesUpdateView, ServicesDetailView, ServicesDeleteView, ServicesDeletedList, ServicesPublicListView

from deals.views import ServiceDealView, AffiliateDealView, ServiceDealSellerListView, ServiceDealBuyerListView, ThanksPageListView


deals_patterns = [
    
    url(_(r'^deals/create/a/(?P<slug>[\w-]+)/$'), AffiliateDealView.as_view(), name="affiliates"),
    url(_(r'^deals/create/(?P<slug>[\w-]+)/$'), ServiceDealView.as_view(), name="create"),
    url(_(r'^deals/sell/list/$'), ServiceDealSellerListView.as_view(), name="seller_list"),
    url(_(r'^deals/buy/list/$'), ServiceDealBuyerListView.as_view(), name="buyer_list"),
    url(_(r'^deals/thanks/$'), ThanksPageListView.as_view(), name="thanks"),
    
]



services_patterns = [


    url(_(r'^services/create/(?P<slug>[\w-]+)$'), ServicesCreateView.as_view(), name="create"),
    url(_(r'^services/briefcase/$'), ServicesListView.as_view(), name="my_list"),
    url(_(r'^services/briefcase/edit/(?P<slug>[\w-]+)/$'), ServicesUpdateView.as_view(), name="edit"),
    url(_(r'^services/(?P<slug>[\w-]+)/$'), ServicesDetailView.as_view(), name="detail"),
    url(_(r'^services/delete/(?P<pk>\d+)/$'), ServicesDeleteView.as_view(), name="delete"),
    url(_(r'^services/deleted/list/$'), ServicesDeletedList.as_view(), name="delete_list"),
    url(_(r'^$'), ServicesPublicListView.as_view(), name="list"),

]



companies_patterns = [


    url(_(r'^affiliates/$'), AffiliatesPublicListView.as_view(), name="list"),
    url(_(r'^affiliates/create/$'), AffiliatesCreateView.as_view(), name="create"),
    url(_(r'^affiliates/companies/$'), AffiliatesListView.as_view(), name="my_list"),
    url(_(r'^affiliates/update/(?P<slug>[\w-]+)/$'), AffiliatesUpdateView.as_view(), name="update"),
    url(_(r'^affiliates/(?P<slug>[\w-]+)/$'), AffiliatesDetailView.as_view(), name="detail"),
    url(_(r'^affiliates/delete/(?P<pk>\d+)/$'), AffiliatesDeleteView.as_view(), name="delete"),
    url(_(r'^affiliates/delete/list/$'), AffiliatesDeletedList.as_view(), name="delete_list"),

]


urlpatterns = [
	
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^u/', include('accounts.urls', namespace='profiles')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    

]

urlpatterns += i18n_patterns(

    
    url(_(r'^'), include(companies_patterns, namespace='affiliates')),
    url(_(r'^'), include(services_patterns, namespace='services')),
    url(_(r'^'), include(deals_patterns, namespace='deals')), 


)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)