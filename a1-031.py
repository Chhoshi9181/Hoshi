s = input()

result = ""
count = 0

for i in range(len(s)-1, -1, -1):
    result = s[i] + result
    count += 1
    if count % 3 == 0 and i != 0:
        result = "," + result

print(result)