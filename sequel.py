from collections import defaultdict
from _reader     import update_dict, update_rdict, generate_prgsn, generate_rhythm
from _inputter   import input_int, input_yn
from _converter  import to_mxml, build_class, FileContents

if __name__ == '__main__':
   
    pattern_dict = defaultdict(set)
    song_chd_dict = defaultdict(set)
    rhythm_dict = defaultdict(set)
    song_rtm_dict = defaultdict(set)
    
    weight = input_int("Select weight of progression", legal = (lambda x: x > 0))

    print("Parsing the files...\n")

    update_dict( pattern_dict , weight , song_chd_dict )
    update_rdict( rhythm_dict , song_rtm_dict)
    #print( song_chd_dict)    

    pattern_dict = dict(pattern_dict)
    rhythm_dict = dict(rhythm_dict)
    print(rhythm_dict)

    if pattern_dict == {}:
        print('No files were processed, so generating a progression is impossible.')
    
    else:
        prog_len = input_int("Choose number of chords in the progression", legal = (lambda x: x >= weight), error_msg='Number of chords must be greater than the specified weight.')

        print("Generating progression...\n")

        the_progression = generate_prgsn(pattern_dict, song_chd_dict, weight, prog_len, True)
        the_rhythms = generate_rhythm(rhythm_dict, song_rtm_dict, prog_len, True)
       
        print("Progression generated successfully!")
        print("Processing data...\n")
        
        song = [x for x in zip(the_progression, the_rhythms)]
        p = build_class(song)
        print('\n')
        
        k = FileContents(title = 'hello', progression = p)
       
        with open('out.xml', 'w') as the_file:
            try:
                xmlgen = k.the_xml()
                numlines = next(xmlgen)
                lenth = len(str(numlines))
                count = 1
                for line in xmlgen:
                    the_file.write(line + '\n')
                    print(f'Lines written: %{lenth}s / {numlines}    ' % count , end = '\r')
                    count += 1

                print('\n\nWritten successfully to out.xml.\n')
            except StopIteration:
                print('Error occurred.\n')
            
        
        print('Done.')
        



