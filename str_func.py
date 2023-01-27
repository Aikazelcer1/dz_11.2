#!/usr/bin/python3
def initials(name):
    words = name.split()
    result = "" 
    for word in words:
        result += word[0].upper()
    return result

string = input().split()
lst = []
for i in string:
    lst.append(i.capitalize())
print(' '.join(lst))

