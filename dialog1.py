import datetime
name = input("What is your name?: ")
birth_year = int(input("Great to meet you, " + name + "!  What year were you born?: "))
now = datetime.datetime.now()
numb1 = (now.year - birth_year) -1
numb2 = now.year - birth_year
print("Oh, " + str(birth_year) + ". That makes you either " + str(numb1) + " or " + str(numb2) + " years old.")
