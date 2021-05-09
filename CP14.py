# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_sq(n):
    sum1 = 0
    for i in range(n):
        sum1 = sum1+i**2
    return sum1


x = int(input())
print(sum_sq(x))


def sum_squ(n):
    return sum([i * i for i in range(0, n)])


print(sum_squ(56))