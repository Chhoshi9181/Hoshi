
try:
    size, type = map(str, input().split())
    topping_input = input()
    total = 0
    num = 0

    if size == 'S':
        if type == 'R':
            total += 60
        else:
            total += 80
    elif size == 'M':
        if type == 'R':
            total += 80
        else:
            total += 100
    elif size == 'L':
        if type == 'R':
            total += 100
        else:
            total += 120

    if topping_input != 'N':
        topping_parts = topping_input.split()
        if len(topping_parts) == 2:
            top, num = topping_parts
            num = int(num)
            if top == 'P':
                total += 15 * num
            elif top == 'E':
                total += 10 * num

    print(total)
except:
    print(0)
