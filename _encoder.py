import re

# _encoder.py - this module contains data to map notes to integers.

NOTE_IDX = {'C': 0,
            'D': 2,
            'E': 4,
            'F': 5,
            'G': 7,
            'A': 9,
            'B': 11}

NOTE_IDW = {0 :'C',
            2 :'D',
            4 :'E',
            5 :'F',
            7 :'G',
            9 :'A',
            11:'B'}





NOTE_ORD = ['C','D','E','F','G','A','B']

ACCID = {'' :  0,
         'b': -1,
         '#':  1,
         '%': -2,
         'x':  2}

# ACCIDW uses -1 === 11 mod 12 and -2 === 10 mod 12.
# % : double flat, x : double sharp
ACCIDW = { 0:'',

          11:'b',
          -1:'b',

           1:'#',

          10:'%',
          -2:'%',

           2:'x'}
# CHORDS dict maps type to (index relative to first note , note relative to first note), (allowed notes, passing)
#CHORDS = {'maj7' :  ( (0, 4, 7, 11)     , (0, 2, 4, 6)    ) , (something),
#          '7'    :  ( (0, 4, 7, 10)     , (0, 2, 4, 6)    ) , (...),
#          '-7'   :  ( (0, 3, 7, 10)     , (0, 2, 4, 6)    ) , (...),
#          '-7b5' :  ( (0, 3, 6, 10)     , (0, 2, 4, 6)    ) , (...),
#          ''     :  ( (0, 4, 7)         , (0, 2, 4)       ) , (...),
#          'm'    :  ( (0, 3, 7)         , (0, 2, 4)       ) , (...),
#          'm9'   :  ( (0, 3, 7, 10, 14) , (0, 2, 4, 6, 8) ) , (...)}
CHORDS = {}

with open('chords.txt' ) as chd_file:
    for line in chd_file:
        if line[0] == '#':
            continue
        #chdn, left, right, notes, passing = line.rstrip().split(':')
        chdn, *right = line.rstrip().split(':')
        CHORDS[chdn.strip()] = tuple( tuple(int(s) for s in sect.split()) for sect in right)

CHORD = re.compile(r'^([A-G])([b#%x]?)(' + '|'.join(CHORDS) + ')$')

