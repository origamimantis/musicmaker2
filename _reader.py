from collections import defaultdict, deque
from pathlib import Path
from random  import choice as randchoice



# _reader.py - this module handles the parsing of files containing chord progressions
#              and stores them in a dictionary-like object using frozensets as keys.


def parse_file(pattern_dict: defaultdict , weight : int, the_file : open) -> {(str):[str]}:
    '''Reads a given file and generates a dictionary mapping partial progressions to possible chords.'''
    
    gen = _chord_gen(the_file)
    
    current_phrase = deque((next(gen) for x in range(weight)) , maxlen = weight)
    
    for chord in gen:

        pattern_dict[tuple(current_phrase)].add(chord)

        current_phrase.popleft()
        current_phrase.append(chord)


def _chord_gen(file : open):
    '''Generator that yields each chord in a file.'''

    for line in file:
        for item in line.split(','):
            yield frozenset(item.strip()[1:-1].split(';'))


def update_dict(pattern_dict, weight, directory = "files"):
    
    for progfile in Path(directory).iterdir():

        with open(progfile, 'r') as the_file:
            try:
                parse_file( pattern_dict, weight, the_file)
            except RuntimeError:
                pass


def generate_prgsn(pattern_dict: {(str):[str]}, weight: int, total_len: int , curl: bool = False) -> [str]:
    '''Generates and returns list of chord progressions; option to continue if next chord isn't found.'''
    
    prgsn = list(randchoice(tuple(pattern_dict.keys())))
   
    c = weight

    while c < total_len:
        try:
            k =  randchoice(tuple(pattern_dict[  tuple(prgsn[-weight:])  ]  ))
            prgsn.append(k)
            c += 1
            
        except IndexError:
            if curl:
                h =   randchoice( tuple( pattern_dict.keys() ))
                prgsn.extend(h)
                
                
                c += weight 
            else:
                prgsn.append(None)
                break

    return prgsn[:total_len]

