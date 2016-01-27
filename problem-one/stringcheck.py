#!/usr/bin/env python3

def checkString(sstr, sset):
    """ 
    Return the index of the first occurence of a character from sset in sstr
    """
    lookup = [False for i in range(0,255)]
    for char in sset:
        if 0 <= ord(char)<len(lookup): lookup[ord(char)] = True
    i = 0
    while i<len(sstr):
        if lookup[ord(sstr[i])]: return i;
        i+=1
    return len(sstr)
