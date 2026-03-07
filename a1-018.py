n = int(input())

if n < 0:
    print("Error : Please input positive number")
elif n == 0 or n > 9:
    print("Error : Out of range")
else:
    roman = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    print(roman[n])