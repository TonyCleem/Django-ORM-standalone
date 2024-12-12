import os
import django
import datetime
from django.utils.timezone import localtime
from timer import get_duration, format_duration


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
    # visits = Visit.objects.filter(leaved_at__isnull=True)
    # for visit in visits:
    #     employee_name = visit.passcard.owner_name
    #     entered_at = visit.entered_at
    #     string_entered_at = entered_at.strftime("%m/%d/%Y, %H:%M:%S")
    #     duration = get_duration(visit)
    #     duration = format_duration(duration)
    #     print(duration)

    # # Шаг 12
    # visits = Visit.objects.filter(leaved_at__isnull=True)
    # for visit in visits:
    #     employee_name = str(visit.passcard.owner_name)
    #     entered_at = visit.entered_at
    #     duration = get_duration(visit)
    #     duration = format_duration(duration)

    #     months = {
    #             1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
    #             7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    #         }

    #     entered_at = f"{entered_at.day} {months[entered_at.month]} {entered_at.year} г. {entered_at.strftime('%H:%M')}"


        # Шаг 13





   


   

