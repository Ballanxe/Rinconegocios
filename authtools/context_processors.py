from django.utils.translation import ugettext_lazy as _
from authtools.forms import AuthenticationForm, UserCreationForm, CaseInsensitiveUsernameFieldCreationForm
from deals.forms import ServiceDealForm

def include_forms(request):
    login_form = AuthenticationForm
    # print(login_form)
    register_form = CaseInsensitiveUsernameFieldCreationForm(request.POST)

    if request.user.is_authenticated:
    	deal_form = ServiceDealForm(initial={'name':request.user.first_name,'email':request.user.email, 'last_name':request.user.last_name, 'phone':request.user.phone, 'message':_('Hola quisiera recibir más informacion'), })

    	return {'login_form': login_form, 'register_form':register_form, 'deal_form':deal_form}


    return {'login_form': login_form, 'register_form':register_form}


