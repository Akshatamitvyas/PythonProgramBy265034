# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(n):
    if (-1)**n == 1:
        return True
    else:
        return False


t = int(input())
for i in range(t):
    x = int(input())
    print(is_even(x))