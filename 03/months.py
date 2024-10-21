# The program outputs a number of days of a month given by user
month = input("Input a name of a month: ").lower()

if month == "february":
    print("Number of days: 28/29")
elif month == "april" or month == "june" or month == "september" or month == "november":
    print("Number of days: 30")
elif month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    print("Number of days: 31")
else:
    print("Invalid month name") 
