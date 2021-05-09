# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def odd_pro(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
                p = n[i] * n[j]
            if p & 1:
                return True
            return False


t = int(input())
for k in range(t):
    li = list(map(int, input().split()))
    print(odd_pro(li))