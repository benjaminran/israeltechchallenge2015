#!/usr/bin/env python3
import stringcheck
import unittest
import string
import random
import timeit


class TestStringCheck(unittest.TestCase):
    

    def test_correct(self):
        """ Tests that output is the same for the 2 implementations on 1000 sets of randomly generated inputs """
        reps = 10
        while reps>0:
            sstr = rand_string(random.randint(10, 1000000))
            sset = rand_string(random.randint(1,256))
            re = run_re(sstr, sset)
            hash = run_hash(sstr, sset)
            self.assertTrue(re == hash)
            reps -= 1
            

    def test_time_re(self):
        """ Test that the algorithm runs in time O(m+n). If time(checkstringForSet(m,n))/(m+n) does not diverge to infinity as m and n grow large, the algorithm is likely O(m+n). This is, of course, not necesssarily correct for many reasons, but is hopefully a fair estimate. """
        set_len = 1;
        str_len = 8;
        times = []
        while set_len < 128:
            time = runtime_hash(str_len, set_len)
            output = 10000 * time / (str_len+set_len)
            print(str.format("(m,n)=({0},{1}); time/(m+n) = {2}", str_len, set_len, output))
            times.append(output)
            str_len *= 8
            set_len *= 2
        self.assertTrue(times[-1] < times[0])
            
            
def runtime_hash(n, m):
    """ Runs string-check once with len(sstr)=n and len(sset)=m and returns a very simple benchmark """
    sstr = rand_string(n)
    sset = rand_string(m)
    invocation = str.format("stringcheck.checkStringForSet('{0}','{1}')", sstr, sset)
    return timeit.timeit(invocation, setup="import stringcheck", number=1000)


def rand_string(size):
    return ''.join(random.choice(string.ascii_letters) for x in range(size))


def run_re(sstr, sset):
    return stringcheck.checkStringForSetRe(sstr, sset)


def run_hash(sstr, sset):
    return stringcheck.checkStringForSet(sstr, sset)

if __name__ == "__main__":
    unittest.main()
