# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n≤k<0, what is the equivalent index j ≥0 such that s[j] references
# the same element?

def rev_str(s):
    x = len(s)
    for i in range(-x, 0):
        print(s[i])
    for j in range(-x, 0):
        print(s[j + x])


n = input()
print(rev_str(n))