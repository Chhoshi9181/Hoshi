temp = int(input())
unit = input().strip().lower()

# แปลงเป็น Celsius ถ้าเป็น Fahrenheit
if unit == 'f':
    temp = (temp - 32) * 5 / 9

# ตรวจสถานะ
if temp <= 0:
    print("solid")
elif temp < 100:
    print("liquid")
else:
    print("gas")