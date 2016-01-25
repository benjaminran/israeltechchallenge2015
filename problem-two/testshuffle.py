#!/usr/bin/env python3
import unittest
import random
import sys
import shuffle

class ShuffleTest(unittest.TestCase):

    def testshuffle(self):
        """ Tests for runtime errors and prints a sample shuffled list """
        reps = 1000
        while reps>0:
            output = shuffle.knuthshuffle(self.constructlist(random.randint(0,1000)))
            if reps == 1: print("Sample output: " + str(output))
            reps -= 1

    def constructlist(self, size):
        return [i for i in range(size)]


if __name__ == "__main__":
    unittest.main()
