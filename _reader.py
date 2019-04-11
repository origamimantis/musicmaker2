from collections import defaultdict, deque
from pathlib import Path


def chord_gen(file : open):
    '''Generator that yields each chord in a file.'''

    for line in file:
        for item in line.split(','):
            yield frozenset(item.strip()[1:-1].split(';'))


def parse_file(pattern_dict: defaultdict , weight : int, the_file : open) -> {(str):[str]}:
    '''Reads a given file and generates a dictionary mapping partial progressions to possible chords.'''
    
    gen = chord_gen(the_file)
    
    current_phrase = deque((next(gen) for x in range(weight)) , maxlen = weight)
    
    for chord in gen:

        pattern_dict[tuple(current_phrase)].add(chord)

        current_phrase.popleft()
        current_phrase.append(chord)

def update_dict(pattern_dict, weight, directory = "files"):
    
    for progfile in Path(directory).iterdir():

        with open(progfile, 'r') as the_file:
            try:
                parse_file( pattern_dict, weight, the_file)
            except RuntimeError:
                pass



