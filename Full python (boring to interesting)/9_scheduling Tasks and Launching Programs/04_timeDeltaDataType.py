# Time delta data type represents a duration of time ratyher tham the time.
# weeks, days, hours, minutes, seconds, milliseconds, microseconds.
import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=6)
print(delta.days, delta.seconds, delta.microseconds)

print(delta.total_seconds())
print(str(delta))

print('======================')

dt = datetime.datetime.now()
print(dt)

thousandDays = datetime.timedelta(days=1000)
print(dt+thousandDays)			# Thousand days from now.