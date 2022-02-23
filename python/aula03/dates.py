def isLeapYear(year):
    if year%4 == 0 and year%400==0 and year%100==0:
        print('O ano {} é bissexto'.format(year))
        return True
    else:
        print('O ano {} é comum'.format(year))
        return False
def monthDays(year, month):
    if isLeapYear(year):
        MONTHDAYS = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        days = MONTHDAYS[month]
        return days
    else:
        MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            # This tuple contains the days in each month (on a common year).
            # For example: MONTHDAYS[3] is the number of days in March.
        days = MONTHDAYS[month]
        return days
def nextDay(day, month, year):
    monthdays = monthDays(year, month)

    if month == 12 and day == 31:
        return 1, 1, year + 1
    if day < monthdays:
        return day + 1, month, year
    else:
        return 1, month + 1, year
def main():
    dia =int(input('dia?'))
    mes =int(input('mês?'))
    ano =int(input('ano?'))

    d,m,a =nextDay(dia,mes,ano)
    print(d,m,a)   
        
main()