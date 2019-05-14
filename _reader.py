from collections import defaultdict, deque
from pathlib import Path
from random  import choice as randchoice



# _reader.py - this module handles the parsing of files containing chord progressions
#              and stores them in a dictionary-like object using frozensets as keys.


def parse_file(pattern_dict: defaultdict , weight : int, the_file, fname , ptype , songchords:defaultdict = None ):
    '''Reads a given file and generates a dictionary mapping partial progressions to possible chords.'''
    
    gen = _chord_gen(the_file)
   
    # Will raise RuntimeError (StopIteration) if weight > #chords in file.
    current_phrase = deque((next(gen) for x in range(weight)) , maxlen = weight)
    
    
    for chord in gen:
        
        songchords[fname].add(tuple(current_phrase))
        
        pattern_dict[tuple(current_phrase)].add(chord)
        current_phrase.popleft()
        current_phrase.append(chord)
    songchords[fname].add(tuple(current_phrase))

def parse_rhy(rtmlist, the_file):
    ''' Read lines of a file and extract common rhythms'''

    for line in the_file:
        if not line.isspace():
            k = line.split()
            rtmlist.append(tuple(k))


def _chord_gen(the_file : open):
    '''Generator that yields each chord in a file.'''

    for line in the_file:
        chd, name = line.rstrip().split()
        yield name, frozenset(chd.strip()[1:-1].split(';'))


def update_dict(pattern_dict, weight, songchords,directory = "files"):
    '''populate chords dict with chords from files.'''
    failed = False
    for progfile in Path(directory).iterdir():

        if progfile.is_file():
            with open(progfile, 'r') as the_file:
                try:
                    parse_file( pattern_dict, weight, the_file, progfile.name, directory, songchords)
                except RuntimeError:
                    failed = True
                    print(f'{progfile.name} was not parsed because it has less chords in it than the specified weight.')
    if failed: print()


def update_rlist(rtmlist, directory = 'rhythms'):
    for rhyfile in Path(directory).iterdir():
        if rhyfile.is_file():
            with open(rhyfile) as the_file:
                try:
                    parse_rhy(rtmlist, the_file)
                except AssertionError:
                    pass


def generate_prgsn(pattern_dict, song_chd_dict, weight: int, total_len: int , curl: bool = False) -> [str]:
    '''Generates and returns list of chord progressions; option to continue if next chord isn't found.'''
    
    prgsn = list(randchoice(tuple(pattern_dict.keys())))
    failed = False 

    while len(prgsn) < total_len:
        try:
            k =  randchoice(tuple(pattern_dict[  tuple(prgsn[-weight:])  ]  ))
            prgsn.append(k)
        
        # IndexError because at this point pattern_dict is a dict and not a dict, and 
        except KeyError:
            failed = True
            print(f'Unable to find next chord at chord {len(prgsn)}, choosing new seed.')
            if curl:
                h =  randchoice( tuple(song_chd_dict))
                prgsn.extend(randchoice(tuple(song_chd_dict[ h ])))
                print(h)
                
            else: break
    if failed: print()

    return prgsn[:total_len]


def generate_rhythm(rhythmslist, total_len: int , curl: bool = False) -> [str]:
    '''Generates and returns list of chord progressions; option to continue if next chord isn't found.'''
  
    rtms = []

    while len(rtms) < total_len:
        k =  randchoice(rhythmslist)
        rtms.extend(k)

    return rtms[:total_len]

