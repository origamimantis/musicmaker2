from random import choice as randchoice



# _patterner.py - this module contains (one) function(s?) to generate a chord progression,
#                 by looking at the n latest chords and choosing a chord to follow it.


def patt_as_str(pattern_dict : {(str):[str]}) -> str:
    
    prgsn_lens = tuple(len(ls) for ls in pattern_dict.values())
    
    return ''.join("  " + '[' + ', '.join(str(set(chd)) for chd in phrase) + "] precedes by any of [" + ', '.join(str(set(nex)) for nex in pattern_dict[phrase]) + ']\n' for phrase in pattern_dict)



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
#[set(chd) for chd in prgsn][:total_len]


