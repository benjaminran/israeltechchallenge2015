#!/usr/bin/env python3
import re


def checkStringForSet(sstr, sset):
    """
    Returns the index of the first occurrence of any character from set 
    in str or -1 if no occurrences are found
    """
    regex = '['
    for c in sset: regex += '"' + c + '"'
    regex += ']'
    match = re.compile(regex).search(sstr)
    return match.start() if match else -1
