# Write a Python script to merge two Python dictionaries

def merge(x,y):
    r={**x,**y}
    return r
dict1={'1':"Sun",'2':[1,2,3]}
dict2={'3':"Mon",'4':[4,5,6]}
dict3=merge(dict1,dict2)
print(dict3)