
### Dates ###
from datetime import timedelta ##para operar y trabajar con diferencias de fechas / Diferencias de tiempo (sumas/restas de fechas u horas)
from datetime import date ## unicamente una fecha (año, mes, día)
from datetime import time ## representar unicamente una hora (hora, minuto, segundo, microsegundo)
from datetime import datetime ##representar tanto fecha como hora (año, mes, día, hora, minuto, segundo, microsegundo)

fecha_actual = date.today()  # fecha actual
print(fecha_actual)  # salida: la fecha actual

hora_actual = time(14, 30, 15)  # 14:30:15
print(hora_actual)  # salida: 14:30:15

fecha_hora_actual = datetime.now()  # obtener la fecha y hora actual
print(fecha_hora_actual)  # salida: fecha y hora actual


now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# Time


current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date


current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)

# Operaciones con fechas

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# Timedelta
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
