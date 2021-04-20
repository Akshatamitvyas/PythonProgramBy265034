#Use of the map() function
def add_five(x):
    return x+5
m=list(map(int,input().split()))
r=list(map(add_five,m))
print(r)