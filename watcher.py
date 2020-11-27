import datetime
from os import system
while True:
	system("cls")
	time = datetime.datetime.now()
	dates = open("dates.py", "r")
	today_date = dates.read().split("\n")[time.weekday()]
	today_date_arr = today_date.split(" ")
	shutdown = True
	for date in today_date_arr:
		if date != "":
			start_time = date.split("-")[0]
			finish_time = date.split("-")[1]
			start_time_hour_and_minute = start_time.split(":")
			finish_time_hour_and_minute = finish_time.split(":")
			if time.hour in range(int(start_time_hour_and_minute[0]), int(finish_time_hour_and_minute[0]) + 1):
				if not(time.hour == int(start_time_hour_and_minute[0]) and time.minute < int(start_time_hour_and_minute[1])):
					if not(time.hour == int(finish_time_hour_and_minute[0]) and time.minute > int(finish_time_hour_and_minute[1])):
						shutdown = False
						break
	if shutdown:
		print("SHUTDOWN")
		#system("shutdown /s")