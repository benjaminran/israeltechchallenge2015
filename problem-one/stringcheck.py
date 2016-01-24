#!/usr/bin/env python3
import re

def checkStringForSet(sstr, sset):
    """
    Returns the index of the first occurrence of any character from sset 
    in sstr or -1 if no occurrences are found

    This implementation uses a dictionary of the characters in sset 
    (constructed in O(m) time) and checks each character in sstr to see 
    if it is in the dict. Assuming the dict is implemented as a hashmap 
    (with amortized access time O(1)), the time of this implementation 
    should be O(n+m).
    """
    map = { c : True for c in sset}
    i = 0
    while i<len(sstr):
        if map.get(sstr[i], False): return i;
        i+=1
    return -1
    

def checkStringForSetRe(sstr, sset):
    """
    Returns the index of the first occurrence of any character from sset 
    in sstr or -1 if no occurrences are found

    This implementation constructs a regular expression based off the 
    characters in sset and uses it to search sstr
    """
    regex = '['
    for c in sset: regex += '"' + c + '"'
    regex += ']'
    match = re.compile(regex).search(sstr)
    return match.start() if match else -1

if __name__ == "__main__":
    print(checkStringForSet('string', 'efg'))
