#!/usr/bin/env python3
import sys
import random

def knuthshuffle(songs):
   """ Shuffle the elements in an list of songs """
   i = 0
   while i<len(songs)-1:
      swap(songs, i, random.randint(i, len(songs)-1))
      i += 1
   return array

def swap(songs, a, b):
   temp = songs[a]
   songs[a] = songs[b]
   songs[b] = temp
