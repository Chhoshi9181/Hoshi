import math

def parse_time(t):
    try:
        h, m = t.split('.')
        h = int(h)
        m = int(m)
    except:
        return None
    
    if not (0 <= h <= 23 and 0 <= m <= 59):
        return None
    
    return h * 60 + m


i = input().strip()
o = input().strip()

start = parse_time(i)
end = parse_time(o)

# ตรวจ error
if start is None or end is None or start >= end:
    print("ERROR")
else:
    duration = end - start
    
    if duration < 15:
        print("FREE")
    else:
        hours = math.ceil(duration / 60)
        
        if hours == 1:
            print(25)
        elif hours == 2:
            print(50)
        elif hours == 3:
            print(80)
        elif hours == 4:
            print(110)
        elif hours == 5:
            print(145)
        elif hours == 6:
            print(180)
        else:
            print(250)