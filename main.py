import os
import django
import datetime
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard
from datacenter.models import Visit # noqa: E402


if __name__ == '__main__':
    #шаг 10
    # current_time =  localtime().replace(microsecond=0)
    # employees_from_storage = Visit.objects.filter(leaved_at__isnull=True)

    # for employee in employees_from_storage:
    #     print(f'{employee.passcard} - Зашёл в хранилище, время по Москве:')
    #     print(employee.entered_at)
    #     print()
    #     stay_time = current_time - employee.entered_at
    #     print("Находится в хранилище:")
    #     print(stay_time)

    #шаг 11
    employees_from_storage = Visit.objects.filter(leaved_at__isnull=True)
    for employee in employees_from_storage:
        employee_name = employee.passcard.owner_name
        print(employee_name)

   


   

