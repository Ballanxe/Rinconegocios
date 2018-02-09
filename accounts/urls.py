from django.conf.urls import url
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from .views import ProfileDetailView


urlpatterns = [

	url(r'^(?P<pk>\d+)/$', ProfileDetailView.as_view(), name="detail"), 

]
