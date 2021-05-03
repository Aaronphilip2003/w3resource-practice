from datetime import date

f_year=int(input("Enter the initial year:"))
f_month=int(input("Enter the initial month:"))
f_day=int(input("Enter the initial day:"))

l_year=int(input("Enter the final year:"))
l_month=int(input("Enter the final month:"))
l_day=int(input("Enter the final day:"))

f_date=date(f_year,f_month,f_day)
l_date=date(l_year,l_month,l_day)

difference=l_date-f_date

print("Days in between:",difference.days)
