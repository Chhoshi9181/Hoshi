name = input()
lastname = input()
age = input()

if len(name) > 5 and len(lastname) > 5:
    password = name[:2] + lastname[-1] + age[-1]
else:
    password = name[0] + age + lastname[-1]

print(password)