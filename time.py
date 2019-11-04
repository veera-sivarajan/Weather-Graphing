from datetime import datetime
def get_time():
    hour = ""
    time = str(datetime.now())
    for digit in time[11:13]:
	    if digit.isnumeric():
		    hour += digit
    return hour