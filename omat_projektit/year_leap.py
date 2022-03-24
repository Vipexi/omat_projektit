#! /usr/bin/python3

def is_leap(year):
    leap = False
    
    if year % 4 ==0:  
        return False
    elif year & 4 == 0 and year % 100 == 0: 
        return False
    elif year & 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return leap

year = int(input("Give year: "))
print(is_leap(year))
