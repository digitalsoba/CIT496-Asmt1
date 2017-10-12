#!/usr/local/bin/python3

from collections import OrderedDict

OUTPUTFILE = 'colTrans.txt'

def attack(words):
    with open(OUTPUTFILE) as data_file:
        results = {}

        for line in data_file:
            cols, string = line.strip().split(',')
            results[string] = []

            for _word in words:
                word = _word.strip().upper()

                if len(word) < 3:
                    continue

                if word in string:
                    results[string].append(word)

        sortedResults = OrderedDict(sorted(results.iteritems(), key=lambda x: len(x[1]), reverse=True))

def dictionary():

    some_words = []
    with open('/usr/share/dict/words','r') as dict:
        some_words = dict.read().split()
    return some_words

attack(dictionary())