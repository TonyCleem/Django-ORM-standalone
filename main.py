import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard
from datacenter.models import Visit # noqa: E402


if __name__ == '__main__':

    
    not_leaved_visits = Visit.objects.filter(leaved_at__isnull=True)
    print(not_leaved_visits)

   

