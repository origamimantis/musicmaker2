from _inputter import input_yn
from pathlib import Path
import re


# _cp_to_file.py - Script to write chords written in a common format to a format that sequel.py can read.

NOTE_IDX = {'C': 0,
            'D': 2,
            'E': 4,
            'F': 5,
            'G': 7,
            'A': 9,
            'B': 11}

NOTE_ORD = ['C','D','E','F','G','A','B']

ACCID = {'' :  0,
         'b': -1,
         '#':  1,
         '%': -2,
         'x':  2}

# ACCIDW uses -1 === 11 mod 12 and -2 === 10 mod 12.

ACCIDW = { 0:'',

          11:'b',
          -1:'b',

           1:'#',

          10:'%',
          -2:'%',

           2:'x'}


# CHORDS dict maps type to (index relative to first note , note relative to first note)

CHORDS = {'maj7' :  ( (0, 4, 7, 11) , (0, 2, 4, 6) ) ,
          '7'    :  ( (0, 4, 7, 10) , (0, 2, 4, 6) ) ,
          '-7'   :  ( (0, 3, 7, 10) , (0, 2, 4, 6) ) ,
          '-7b5' :  ( (0, 3, 6, 10) , (0, 2, 4, 6) ) ,
          ''     :  ( (0, 4, 7)     , (0, 2, 4)    ) ,
          'm'    :  ( (0, 3, 7)     , (0, 2, 4)    ) }


class ChordsTranslateError(Exception):
    pass

def _translated(chord):
    if chord[0] not in 'ABCDEFG':
        raise ChordsTranslateError
    
    base = NOTE_IDX[chord[0]]
    bsidx = NOTE_ORD.index(chord[0])
    chdt = chord[1:]
    try:
        if chord[1] in 'b#%x':
            base += ACCID[chord[1]]
            chdt = chord[2:]
    # means it's a major chord w/o accidental, like G or A
    except IndexError:
        chdt = ''
        

    ind, rel = CHORDS[chdt]

    notelist = []

    for x in range(len(ind)):
        
        visnote = NOTE_ORD[(bsidx + rel[x] )%7]
        notelist.append( visnote + ACCIDW[(base + ind[x])%12 - NOTE_IDX[visnote]])
        



    return '{' + ';'.join(notelist) + '}\n'




def _parse(line):
    the_list = re.split(r'(?:\s*,?\s+|\s*,\s*)', line)

    parsed_line = ''
    
    for chord in the_list:
        if chord != '':
            parsed_line += _translated(chord)
    return parsed_line


def read( directory = 'to_convert' ):
    for filename in Path(directory).iterdir():
        
        altpath = Path('files') / Path(filename.name)
        if altpath in Path('files').iterdir() and not input_yn(f'Overwrite {filename.name}?', 'No'):
            print(f'Skipped file {filename.name}; continuing to next file, if it exists.')
            continue
        with open(filename, 'r') as old_f, open(altpath, 'w') as new_f:
            for line in old_f:
                try:
                    new_f.write(_parse(line.strip()))
                except StopIteration: #(KeyError, ChordsTranslateError):
                    print(f'Error parsing {filename.name}. Attempting next file, if it exists.')
                    break



if __name__ == '__main__':

    read()

    print("Done.")
