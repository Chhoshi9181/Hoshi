arr = []

# รับค่า 3 ตัว
for i in range(3):
    x = int(input())
    arr.append(x)
    print(f"Input number {i+1} stored.")

# รับเมนู
choice = int(input())

if choice == 1:
    print("Original order:", *arr)

elif choice == 2:
    desc = sorted(arr, reverse=True)
    print("Descending order:", *desc)

elif choice == 3:
    asc = sorted(arr)
    print("Ascending order:", *asc)

elif choice == 0:
    pass