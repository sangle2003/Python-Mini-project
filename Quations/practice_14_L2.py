#check leap year or not.
def leap_year():
    year = int(input("Enter your year :: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Year is a leap year")
    else:
        print("Year is not a leap year")
        
leap_year()