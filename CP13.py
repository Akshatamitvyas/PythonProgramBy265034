# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.
def min_max(n):
    n.sort()
    x = (n[0], n[-1])
    return x


t = list(map(int, input().split()))
print(min_max(t))