from collections import defaultdict
from _reader     import update_dict, update_rlist
from _generator  import generate_prgsn, generate_rhythm, generate_melody
from _inputter   import input_int, input_yn
from _converter  import build_class, Melody, FileContents

if __name__ == '__main__':
   
    pattern_dict = defaultdict(set)
    song_chd_dict = defaultdict(set)
    rhythms = []
    mrhy = []
    
    weight = input_int("Select weight of progression", legal = (lambda x: x > 0))

    print("Parsing the files...\n")

    update_dict( pattern_dict , weight , song_chd_dict )
    update_rlist( rhythms )
    update_rlist( mrhy , directory = 'mrhythms')

    pattern_dict = dict(pattern_dict)

    if pattern_dict == {}:
        print('No files were processed, so generating a progression is impossible.')
    
    else:
        prog_len = input_int("Choose number of measures in the song", legal = (lambda x: x >= weight), error_msg='Number of chords must be greater than the specified weight.')

        print("Generating progression...\n")

        the_rhythms = generate_rhythm(rhythms, prog_len, True)
        the_progression = generate_prgsn(pattern_dict, song_chd_dict, weight, len(the_rhythms), True)
       
        print("Processing data...\n")
        
        song = [(n,c,t) for (n,c),t in zip(the_progression, the_rhythms)]
        s = generate_melody(song,  mrhy)
        
        p = build_class(song)
        
        k = FileContents(title = 'hello', progression = p, melody = Melody(s))
       
        with open('out.xml', 'w') as the_file:
            the_file.write(k.the_xml())

        print('Written successfully to out.xml.\n')
            
        
        print('Done.')
        



