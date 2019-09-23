import datetime
import sys


def add_time(h, m, s):
    now = datetime.datetime.now()
    added = datetime.timedelta(seconds=s, minutes=m, hours=h)
    new_time = now + added
    print(f"The day is {new_time.month}/{new_time.day}/{new_time.year} and the time is {new_time.hour}:{new_time.minute}:{new_time.second}")


add_time(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

