from _inputter import input_yn
from _encoder  import *
from pathlib   import Path


# format_progression.py - Script to write chords written in a common format to a format that sequel.py can read.

class ChordsTranslateError(Exception):
    pass

def _translated(chord, ln, cn, fn):
    
    match = CHORD.match(chord)
    if match is None:
        raise ChordsTranslateError(f"Invalid chord ({chord}) at position {cn}, line {ln} in file '{fn}'.")
    base = NOTE_IDX[match.group(1)] + ACCID[match.group(2)]
    bsidx = NOTE_ORD.index(match.group(1))
    chdt = match.group(3)

    notelist = []
    ind, rel = CHORDS[chdt][:2]
    for x in range(len(ind)):
        
        visnote = NOTE_ORD[(bsidx + rel[x] )%7]
        notelist.append( visnote + ACCIDW[(base + ind[x])%12 - NOTE_IDX[visnote]])
        



    return '{' + ';'.join(notelist) + '}   '+ chord + '\n'




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

    print("Reading files from to_convert/ ...\n")

    read()

    print("Done.")
