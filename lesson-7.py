# import datetime
#
# # date_time = datetime.datetime(2010, 9, 27, hour=12, minute=36, second=51, microsecond=561)
# date_1 = datetime.date(2012, 5, 23)
# time_1 = datetime.time(11, 7, 47)
# date_time = datetime.datetime.combine(date_1, time_1)
# print(f"new date - {date_time.replace(1980)}")
# print(f"object datetime - {date_time}")
# print(f"object date - {date_time.date()}")
# print(f"object time - {date_time.time()}")
# print(f"type - {type(date_time)}")
#
# date_now = datetime.datetime.now()
# time_now = date_now.time()
# date_today = datetime.datetime.today()
# date_data = datetime.date.today()
# print(f"\ndate_now - {date_now}")
# print(f"time_now - {time_now}")
# print(f"date_today - {date_today}")
# print(f"date_data - {date_data}")
# print(f"weekday - {date_data.weekday()}")
# print(f"isoweekday - {date_data.isoweekday()}\n")
#
# date_str = "29/09/2021 11:20"
# print(f"date_time to str - {date_now.strftime('%d.%m.%Y %H:%M')}")
# print(f"date_time to str - {date_now.strptime(date_str, '%d/%m/%Y %H:%M')}")

import os, datetime


def collector(path, res_path):
    res_path = os.path.normpath(res_path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_time = os.path.getmtime(f"{dirpath}\\{file}")
            datetime_file = datetime.datetime.fromtimestamp(file_time)
            file_date = datetime_file.strftime("%d.%m.%Y")
            if os.path.isdir(f"{res_path}\\{file_date}"):
                os.replace(f"{dirpath}\\{file}", f"{res_path}\\{file_date}\\{file}")
            else:
                os.mkdir(f"{res_path}\\{file_date}\\")
                os.replace(f"{dirpath}\\{file}", f"{res_path}\\{file_date}\\{file}")

path = "C:/Windows/Web"
res_path = "C:/"
collector(path, res_path)