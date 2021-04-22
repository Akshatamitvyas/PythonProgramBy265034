def make(l):
    dict1 = c = {}
    for name in l:
        c[name] = {}
        c = c[name]
    return dict1
n=[1,2,3,4,5,6]
print(make(n))