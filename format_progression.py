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
          'm'    :  ( (0, 3, 7)     , (0, 2, 4)    ) ,
          'm9'   :  ( (0, 3, 7, 10, 14) , (0, 2, 4, 6, 8) ) }

CHORD = re.compile(r'([A-G])([b|#|%x]?)(.*)')

class ChordsTranslateError(Exception):
    pass

def _translated(chord, ln, cn, fn):
    
    
    
    #if chord[0] not in 'ABCDEFG':
    #    raise ChordsTranslateError
    # 
    #base = NOTE_IDX[chord[0]]
    #bsidx = NOTE_ORD.index(chord[0])
    #chdt = chord[1:]
    #try:
    #    if chord[1] in 'b#%x':
    #        base += ACCID[chord[1]]
    #        chdt = chord[2:]
    # means it's a major chord w/o accidental, like G or A
    #except IndexError:
    #    chdt = ''
        
    #ind, rel = CHORDS[chdt]
    match = CHORD.match(chord)
    if match is None:
        raise ChordsTranslateError(f"Invalid note ({chord}) at chord {cn}, line {ln} in file '{fn}'.")

    base = NOTE_IDX[match.group(1)] + ACCID[match.group(2)]
    bsidx = NOTE_ORD.index(match.group(1))
    chdt = match.group(3)

    try:
        ind, rel = CHORDS[chdt]
    except KeyError:
        raise ChordsTranslateError(f"Invalid chord type ({chdt}) at chord {cn}, line {ln} in file '{fn}'.")

    notelist = []

    for x in range(len(ind)):
        
        visnote = NOTE_ORD[(bsidx + rel[x] )%7]
        notelist.append( visnote + ACCIDW[(base + ind[x])%12 - NOTE_IDX[visnote]])
        



    return '{' + ';'.join(notelist) + '}\n'




def _parse(line, linenum, fname):
    the_list = re.split(r'(?:\s*,?\s+|\s*,\s*)', line)

    parsed_line = ''
    chordnum = 0
    for chord in the_list:
        if chord != '':
            chordnum += 1
            parsed_line += _translated(chord, linenum, chordnum, fname)
    return parsed_line


def read( directory = 'to_convert' ):
    for filename in Path(directory).iterdir():
        
        fname = filename.name
        altpath = Path('files') / Path(fname)
        
        if altpath in Path('files').iterdir() and not input_yn(f'Overwrite {filename.name}?', 'No'):
            print(f"Skipped file '{filename.name}'; continuing to next file, if it exists.\n")
            continue
        
        with open(filename, 'r') as old_f, open(altpath, 'w') as new_f:
       
            print(f"Processing file '{filename.name}'...", end = '\r')
            linenum = 0
            failed = False
            
            for line in old_f:
                try:
                    linenum += 1
                    new_f.write(_parse(line.strip(), linenum, fname))
                except ChordsTranslateError as chdexcpt:
                    failed = True
                    print('\n' + str(chdexcpt))
                    altpath.unlink()
                    break
            
            if not failed: print(f"Processing file '{filename.name}'... Finished.\n")
            else:          print(f"Error processing file '{filename.name}'.\n")



if __name__ == '__main__':

    print("Reading files from 'to_convert/ ...\n")

    read()

    print("Done.")
