from datetime import datetime
from datetime import timedelta

def date_in_future(integer):
    if isinstance(integer, int):
        now = datetime.now() + timedelta(days=integer)
    else:
        now = datetime.now()
    currentTime = now.strftime("%d-%m-%y %H:%M:%S")
    return currentTime


print(date_in_future([]))
print(date_in_future(2))