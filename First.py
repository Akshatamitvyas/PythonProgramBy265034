x=int(input())
if(x%3==0 and x%5==0):
    print("Hello World")
elif(x%3==0):
    print("Hello")
elif(x%5==0):
    print("World")
else:
    print(x+" is not divisible by 3 and 5")