#!/usr/local/bin/python3

from collections import OrderedDict

INFILE = 'colTrans.txt'

def attack(dictionary):
    pass

def dictionary():

    some_words = []
    with open('/usr/share/dict/words','r') as dict:
        some_words = dict.read().split()
    return some_words

attack(dictionary())