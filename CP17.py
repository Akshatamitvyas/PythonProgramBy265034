# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

def rev_li(l):
    l.sort(reverse = True)
    return l


li = list(map(int, input().split()))
print(rev_li(li))


