d = int(input("ENTER THE DAY : "))
m = int(input("ENTER THE MONTH : "))
y = int(input("ENTER THE YEAR : "))
if ((y % 4 == 0) and (y % 100 != 0)) or ((y % 400 == 0)):
    if (m == 2):
        d1 = 29
    elif (m in (1,3,5,7,8,10,12)):
        d1 = 31
    else:
        d1 = 30
else:
    if m == 2:
        d1 = 28
    elif (m in (1,3,5,7,8,10,12)):
        d1 = 31
    else:
        d1 = 30
if d == 31 and m == 12:
    d = 1
    m = 1
    y = y + 1
elif d1 - d == 0:
    m = m + 1
    d = 1
else:
    d = d + 1
print("NEXT DAY IS : ", d, "/", m, "/", y)