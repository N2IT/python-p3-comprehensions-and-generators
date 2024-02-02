#!/usr/bin/env python3

def return_evens(num_list):
   only_even = [ n for n in num_list if n % 2 == 0 ]
   return only_even
   
def make_exclamation(sentence_list):
    screaming = [ (n + "!") for n in sentence_list if sentence_list != ""]
    return screaming