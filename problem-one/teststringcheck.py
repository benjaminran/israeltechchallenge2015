#!/usr/bin/env python3
import stringcheck
import string
import random
import timeit


def test():
    """
    Test that the algorithm runs in time O(m+n). If time(checkstringForSet(m,n))/(m+n) does not diverge to infinity as m and n grow large, the algorithm is likely O(m+n). This is, of course, not necesssarily correct for many reason, but I hope a fair estimate.
    """
    set_len = 1;
    str_len = 8;
    times = []
    while set_len < 256:
        time = test_iter(str_len, set_len)
        print(str.format("(m,n)=({0},{1}); time/(m+n) = {2}", str_len, set_len, time/(str_len+set_len)))
        times.append(time/(str_len+set_len))
        str_len *= 8
        set_len *= 2
    print(times[7] - times[6])
    print(times[1] - times[0])


def test_iter(n, m):
    """ Runs string-check once with len(sstr)=n and len(sset)=m and returns a very simple benchmark """
    sstr = ''.join(random.choice(string.ascii_letters) for x in range(n))
    sset = ''.join(random.choice(string.ascii_letters) for x in range(m))
    invocation = str.format("stringcheck.checkStringForSet('{0}','{1}')", sstr, sset)
    return timeit.timeit(invocation, setup="import stringcheck", number=1000)


if __name__ == "__main__":
    test()
