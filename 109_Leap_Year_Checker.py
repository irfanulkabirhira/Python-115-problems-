# 107. Leap Year Checker: Write a Python function called is_leap_year that takes a year as input and returns True if it is a leap year and False otherwise. Test the function with different years.

def is_leap_year(year):
    """
    Function to determine if a given year is a leap year.
    
    Parameters:
    year (int): The year to check.
    
    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Test the function with different years
test_years = [1900, 2000, 2004, 2100, 2020, 2023]

for year in test_years:
    print(f"Year {year} is a leap year: {is_leap_year(year)}")
