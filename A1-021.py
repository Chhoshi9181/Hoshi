year = int(input(""))
if year < 1582 and year % 4 == 0:
  print("yes")
elif year < 1582 and year % 4 != 0:
  print("no")
elif year >= 1582 and year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
  print("yes")
elif year >= 1582 and year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
  print("no")
elif year >= 1582 and year % 4 == 0 and year % 100 != 0:
  print("yes")
else:
  print("no")
