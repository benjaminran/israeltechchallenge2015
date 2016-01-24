# Israel Tech Challenge 2015: Problem One

### Statement
In a language of your choosing, write a function that gets a string named str, and a string named set.The function will return the index of the first appearance of any char from set in str.

F.e. - str = "IsraelTechChallenge2015!", set="t98765!", the function will return 22 (index of '5' in str).

Make sure that time complexity isn't larger than the length of both strings - O(m+n). Assume the string only has ASCII characters.

### Solution
The solution is implemented two different ways in `stringcheck.py`.

Let m be the length of `set` and n be the length of `str`.


##### Solution 1

In the first implementation I construct a hashmap with entries for each character in `set`. This takes O(m) time, and then by amortized analysis the hashmap has O(1) access time. Thus, in the worst case, the hashmap is accessed once for every character in `str` (n * 1 times). Therefore, the overall algorithm runs in O(n+m) time.

This implementation is basically a simple case of finite automaton construction for string matching. This implementation is a Python implementation of a deterministic finite automaton for which the start state and all end states are exactly 1 transition apart. If the goal were to handle more than just the individual characters of `set` and, say, instead treat `set` as a regular expression, I could use [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction) to generate a NFA (and even compress it further into a DFA) and then use that to scan the string. Of course, at that point it would probably be best to use a scanner generator like [Flex](http://flex.sourceforge.net/).

##### Solution 2

In the second implementation I construct a regular expression out of the characters in `set` and use Python's `re` package to find the first occurrence of the the regex in `str`. This is used as a reference implementation for testing.

### Testing
The file `teststringcheck.py` tests my implementations for correctness and does some simple benchmarking in order to check the the algorithm isn't clearly slower than O(m+n).

To check correctness I compare the outputs of my two implementations given the same inputs. Inputs are pseudo-randomly generated strings of ascii characters. While it's possible that both algorithms would be incorrect, solution 2 leaves so much of the work up to Python's `re` package that for these purposes I assume it to be correct.

The benchmarking is done by observing the algorithm's running time on size n and m inputs then dividing that time by (n+m) for increasing n and m. If the algorithm's running time grows asymptotically faster than (n+m) then the outputted value should diverge towards infinity for sufficiently large m and n. Of course, 'sufficiently' can't be quantified and it is possible that the the tests don't use sufficiently large values to observe that the output does in fact, diverge.