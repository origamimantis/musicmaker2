from collections import defaultdict
from _reader     import update_dict, update_rlist
from _generator  import generate_prgsn, generate_rhythm, generate_melody
from _inputter   import input_int, input_yn
from _converter  import build_class, FileContents

if __name__ == '__main__':
   
    pattern_dict = defaultdict(set)
    song_chd_dict = defaultdict(set)
    rhythms = []
    
    weight = input_int("Select weight of progression", legal = (lambda x: x > 0))

    print("Parsing the files...\n")

    update_dict( pattern_dict , weight , song_chd_dict )
    update_rlist( rhythms )

    pattern_dict = dict(pattern_dict)

    if pattern_dict == {}:
        print('No files were processed, so generating a progression is impossible.')
    
    else:
        prog_len = input_int("Choose number of chords in the progression", legal = (lambda x: x >= weight), error_msg='Number of chords must be greater than the specified weight.')

        print("Generating progression...\n")

        the_progression = generate_prgsn(pattern_dict, song_chd_dict, weight, prog_len, True)
        the_rhythms = generate_rhythm(rhythms, prog_len, True)
       
        print("Progression generated successfully!")
        print("Processing data...\n")
        
        s = generate_melody((n,c,t) for (n,c),t in zip(the_progression, the_rhythms))
        song = [(n,c,t) for (n,c),t in zip(the_progression, the_rhythms)]
        
        ## TODO: update song with a generate_melody function on each chord -- song 
        #        should be now ( [ (chordname , chord , time) ],  [ (note, time) ] )
        #        When making, consider making song a generator rather than a list.

        p = build_class(song)
        print('\n')
        
        k = FileContents(title = 'hello', progression = p)
       
        with open('out.xml', 'w') as the_file:
            the_file.write(k.the_xml())

        print('Written successfully to out.xml.\n')
            
        
        print('Done.')
        



