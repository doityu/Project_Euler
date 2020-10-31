# うるう年か判断
def isLeap(year):
    if(year % 400 != 0 and year % 100 == 0):
        return False
    elif(year % 4 == 0):
        return True
    return False

month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
             7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
s_year = 1900
e_year = 2000
sun_day = 1 + 6
res = 0
for i in range(s_year, e_year+1):
    if(isLeap(i)):
        month_day[2] = 29
    else:
        month_day[2] = 28
    
    if(i == e_year):
        month_day.pop(12)
    
    for j in month_day.values():
        while sun_day < j :
            sun_day += 7
        sun_day -= j
        if(sun_day == 1 and i != s_year):
            res += 1

print(res)
