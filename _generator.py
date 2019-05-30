from random   import choice as randchoice
from _encoder import *


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

            else: break
    if failed: print()

    return prgsn[:total_len]


def generate_rhythm(rhythmslist, total_len: int , curl: bool = False) -> [str]:
    '''Generates and returns list of rhythms'''
  
    rtms = []
    time = 0
    while time < 4*total_len:
        k =  randchoice(rhythmslist)
        time += sum(k)
        rtms.extend(k)

    return rtms[:total_len*4]


def generate_melody(song, rtmlist):
    '''iterates over a song list. for each tuple, generates melody to accompany it.'''
    REST = 0.2
    l = []
    time = 0
    totaltime = sum(x[2] for x in song)
    song = iter(song)
    curnote = next(song)
    curtime = 0
    while time < totaltime:
        for x in randchoice(rtmlist):
            time += x
            
            n = CHORD.match(curnote[0])

            ind, rel, notes, passing = CHORDS[n.group(3)]
            
            base = NOTE_IDX[n.group(1)] + ACCID[n.group(2)]
            bsidx = NOTE_ORD.index(n.group(1))
            gen =  randchoice(notes*5 + passing)
            sgna = ACCID[n.group(2)]//abs(ACCID[n.group(2)]) if ACCID[n.group(2)] != 0 else 1
            for add in (0, sgna, 2*sgna, -sgna, -2*sgna):
                if gen + add in NOTE_IDW:
                    visnote = NOTE_IDW[gen + add]
                    break
            l.append( (x, visnote + ACCIDW[ add] ) )
            #l.append( visnote + ACCIDW[(base + ind[x])%12 - NOTE_IDX[visnote]])
        
        try:
            while curtime < time:
                curnote = next(song)
                curtime += curnote[2]
        except StopIteration:
            break
        
    while time > totaltime:
        time -= l.pop()[0]
    return l
