import datetime

name = input("Enter Name: ")
print("Name is: "+name)


x = datetime.datetime.now()

year = input("Enter Year of Birth for this user: ")
age = x.year - int(year)
result = x.year+(100-age)
print("This user will be 100 years old in the year: "+ str(result))