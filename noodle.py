#!/usr/local/bin/python3

# Caesar Shift and Col Transposition
import os
import re

from itertools import permutations
from pycipher import Caesar, ColTrans
from collections import OrderedDict

ciphertext = 'HUKUUEUUYREUYYKGRRGNZZKXNGNOLKXTSAQNZYEGNZTRGTOYALSSEHSYGRVSOOLEGIKVKNZOEJYXT'
six = 'BOEOOYOOSLYOSSEALLAHTTERHAHIFERNMUKHTSYAHTNLANISUFMMYBMSALPMIIFYACEPEHTIYDSRN' #Key shift 6 looks the most human readable
outputfile = 'output.txt'

# PyCi Caesar Cipher
def caesar_Salad(ciphertext):
    caesar_shift = {}
    for x in range(1, 26):
        caesar_shift[x] = Caesar(x).decipher(ciphertext)
    return caesar_shift

#PyCi Col Transposition
def colTranspo(text):
    colOrder = create_permutations('01234567')
    colPos = {}

    for order in colOrder:
        colPos[order] = ColTrans(order).decipher(text)
    return colPos

# itertools Permutation keys
def create_permutations(string):
    perm = [''.join(i) for i in permutations(string)]
    return perm


#print (caesar_Salad(ciphertext))
#print (create_permutations('01234567'))
#Run python3 noodle.py > colTrans.txt
one =  (colTranspo(six))
print (one)

# BEHAPPYFORTHEMOMENTTHISMOMENTISYOURLIFEBYKHAYYAMOHANDALSOTHISCLASSISREALLYFUN