import datetime

mar15th = datetime.datetime(2018, 3, 15, 16, 29, 0)
print(mar15th.strftime('%Y/%m/%d %H:%M:%S'))

print(mar15th.strftime('%I:%M: %p'))
print(mar15th.strftime("%B of '%y"))