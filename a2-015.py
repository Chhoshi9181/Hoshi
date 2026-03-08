w, l, n = map(int, input().split())
price = int(input())

perimeter = 2 * (w + l)
total_length = perimeter * n
total_price = total_length * price

print(total_length)
print(total_price)