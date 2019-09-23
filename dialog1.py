import datetime
name = input("What is your name?: ")
birth_year = int(input(f"Great to meet you, {name}!  What year were you born?: "))
now = datetime.datetime.now()
a = (now.year - birth_year) -1
b = now.year - birth_year
print(f"Oh, {birth_year}. That makes you either {a} or {b} years old.")
