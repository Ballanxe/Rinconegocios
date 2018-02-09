from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def file_size(value): 

	size = 3
	limit = int(size) * 1024 * 1024

	if value.size > limit:
		raise ValidationError(_(f'File too large. Size should not exceed {size} MiB.'))

