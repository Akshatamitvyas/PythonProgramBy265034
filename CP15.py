# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sum_odd(n):
    sum1 = 0
    for i in range(0, n):
        if i % 2 != 0:
            sum1 = sum1 + i
    return sum1


t = int(input())
print(sum_odd(t))