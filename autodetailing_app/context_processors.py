from datetime import datetime
from django.utils import timezone


def get_date(request):
    return {'date': timezone.now().strftime('%d-%m-%Y')}
