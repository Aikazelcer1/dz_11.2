#!/usr/bin/python3
def initials(name):
    words = name.split()
    result = "" 
    for word in words:
        result += word[0].upper()
    return result
