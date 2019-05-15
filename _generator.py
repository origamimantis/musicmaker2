from random  import choice as randchoice


# _generator.py - this module handles the generation of random notes.


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

def generate_melody( songlist : [( str,frozenset,"int as str" )] ) -> [ (str,frozenset,str, [(str,str)]) ]:
    '''iterates over a song list. for each tuple, generates melody to accompany it.'''

    # TODO : probably generate list of rhythms first, then pair with notes.

    totaltime = sum(t[2] for t in songlist)
    print(totaltime)
    
    for chdname, chord, time in songlist:
        pass
