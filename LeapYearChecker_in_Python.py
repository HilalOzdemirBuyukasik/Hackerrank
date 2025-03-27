#This Python function determines whether a given year is a leap year based on the Gregorian calendar rules. A leap year occurs every 4 years, except for years divisible by 100 but not 400. The function returns True for leap years and False otherwise. Task: Given a year, return True if it's a leap year, otherwise return False. Input: A year (integer) to check. Output: Boolean value (True or False).

def is_leap(test_year) -> bool:

    if test_year % 4 == 0:
        if test_year % 100 == 0:
            if test_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year_input = int(input('Enter a year: '))
print(is_leap(year_input))  