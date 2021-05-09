# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

n = int(input())
c = 0
while True:
    if n < 0:
        break
    else:
        n = n - 2
        c = c + 1
print(c)