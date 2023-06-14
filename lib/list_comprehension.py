#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [n for n in num_list if n % 2 == 0]
    return  even_list

def make_exclamation(sentence_list):
    word_list = [w + "!" for w in sentence_list]
    return word_list