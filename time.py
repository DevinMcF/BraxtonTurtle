import datetime


def add_time(h, m, s):
    now = datetime.datetime.now()
    added = datetime.timedelta(seconds=s, minutes=m, hours=h)
    newtime = now + added
    print(f"The day is {newtime.month}/{newtime.day}/{newtime.year} and the time is {newtime.hour}:{newtime.minute}:{newtime.second}")


hours = int(input("How many hours to add?: "))
minute = int(input("How many minutes to add?: "))
seconds = int(input("How many seconds to add?: "))
add_time(hours, minute, seconds)
