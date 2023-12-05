def is_leap_year(year):
   
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

user_input = input("Enter a year: ")

try:
    year_to_check = int(user_input)
    result = is_leap_year(year_to_check)
    print(f"{year_to_check} is a leap year: {result}")
except ValueError:
    print("Please enter a valid integer for the year.")














