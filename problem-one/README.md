# Israel Tech Challenge 2016: Problem One

### Statement
In a language of your choosing, write a function that gets a string named str, and a string named set.The function will return the index of the first appearance of any char from set in str.

F.e. - str = "IsraelTechChallenge2015!", set="t98765!", the function will return 22 (index of '5' in str).

Make sure that time complexity isn't larger than the length of both strings - O(m+n). Assume the string only has ASCII characters.

### Solution
The solution is implemented two different ways in `stringcheck.py`.

Let m be the length of `set` and n be the length of `str`.


##### Solution

My solution is implemented in `stringcheck.py`. Because `str` can only contain ascii characters, there are at most 256 different characters that can be found in `str`. As such, my implementation intializes a 256-entry lookup table that has entries set to `True` only when the corresponding ascii value was included in `set`. This takes O(m) time. Next, the algorithm linearly scans through `str` and looks up each character visited in O(1) time, resulting in a O(n) scan. All together, this means that the algorithm runs in O(m+n) time.


##### Testing

I also include `teststringcheck.py`, a set of tests that confirm correctness of the algorithm. A few static tests are run, then I run a dynamic test that compares output from the above implementation with output from an O(mn) reference implementation (`teststringcheck:checkStringRef`) over 1000 randomized variable-length input strings of ascii characters.