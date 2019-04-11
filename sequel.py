from collections import defaultdict
from _reader     import parse_file, update_dict
from _patterner  import patt_as_str, generate_prgsn
from _inputter   import input_int, input_yn
from _converter  import to_mxml

FILE_NAME = 'out.txt'

if __name__ == '__main__':
   
    pattern_dict = defaultdict(set)
    
    weight = input_int("Select weight of progression", legal = (lambda x: x > 0))

    print("Parsing the files...\n")

    update_dict( pattern_dict , weight )    

    print("Possible Progressions\n" + patt_as_str(pattern_dict))


    words_len = input_int("Choose number of chords in the progression", legal = (lambda x: x >= weight))

    print("Generating progression...\n")

    try:
        the_progression = generate_prgsn(pattern_dict, weight, words_len, True)
    except IndexError:
        the_progression  = None
   
    print("Progression generated successfully!\n")
    if input_yn("Print results to console" , default = 'n'):
        print("Random progression =", the_progression)
    print()
    to_mxml(the_progression)   
    write_bool = input_yn("Write progression to file" , default = 'y')
    
    print()
    
    if write_bool:
        print(f"Writing results to {FILE_NAME} ...\n")
        with open(FILE_NAME, 'w') as the_file:

            if the_progression == None: the_progression = []

            for chd in the_progression:
                the_file.write(str(chd) + '\n')

    print('Done.')
    



