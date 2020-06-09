import datetime

nama=input("Enter your name :")
year=int(input("Year :"))
months=int(input("Month :"))
dates=int(input("Date :"))

today = datetime.date.today()
bornday=datetime.date( year, months, dates)
birthday=datetime.date( today.year, months, dates)

if birthday<today:
    yourage=today.year - bornday.year
else :
    yourage=today.year-bornday.year-1

print(today)
print(birthday)
print(bornday)
print(yourage)


