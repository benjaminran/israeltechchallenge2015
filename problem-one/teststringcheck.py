#!/usr/bin/env python3
import unittest
import random
import stringcheck

# A string containing all the ascii characters
all_ascii = "".join([chr(i) for i in range(0, 255)])

class TestStringCheck(unittest.TestCase):

    def test_static(self):
        """ Tests the primary implementation against known static examples """
        self.assertTrue(stringcheck.checkString('Foo bar baz', all_ascii)==0)
        self.assertTrue(stringcheck.checkString('IsraelTechChallenge2015!', 't98765!')==22)
        self.assertTrue(stringcheck.checkString('testing testing', '123')==15)
    
    def test_dynamic(self):
        """ Tests that the primary and the reference implementations yield the same result over 1000 sets of randomly generated inputs """
        reps = 1000
        while reps>0:
            sstr = rand_string(random.randint(10, 1000))
            sset = rand_string(random.randint(1,256))
            ref = checkStringRef(sstr, sset)
            out = stringcheck.checkString(sstr, sset)
            self.assertTrue(ref == out)
            reps -= 1

            
def rand_string(size):
    """ Generate a random string of ascii characters with the specified size """
    return ''.join(random.choice(all_ascii) for x in range(size))

def checkStringRef(sstr, sset):
    """
    Reference implementation of the string search using the re package (note: runs in O(mn) time)
    """
    return min([sstr.index(c) if c in sstr else len(sstr) for c in sset])
    
if __name__ == "__main__":
    unittest.main()


