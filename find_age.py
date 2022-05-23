"""
age calculator
1. input date of birth
2. find today's date

"""

def age_calculator(y, m, d):
    import datetime
    todays_date = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = (todays_date-dob).days/365.25
    print(int(age))
    return age

age_calculator(1996,8,21)