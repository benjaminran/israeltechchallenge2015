# Israel Tech Challenge 2016: Problem Two


### Solution
In `shuffle.py`, I use the [Knuth Shuffle](https://en.wikipedia.org/wiki/Fisher–Yates_shuffle) to randomly permute `songs`. It iterates once through the list, each iteration generating a single random integer between the current index `i` and the last index of the list, `len(songs)-1`. The element at the random index is swapped with the ith element of the list. This algorithm runs in O(n) time and permutes the list in place, wihtout any additional storage overhead.

### Testing
In `testshuffle.py` I've implemented a simple test that generates 1000 lists of random length, permutes them with my algorithm, and checks for runtime errors. 