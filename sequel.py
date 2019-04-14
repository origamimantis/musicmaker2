from collections import defaultdict
from _reader     import parse_file, update_dict, generate_prgsn
from _inputter   import input_int, input_yn
from _converter  import to_mxml, build_class, FileContents


if __name__ == '__main__':
   
    pattern_dict = defaultdict(set)
    
    weight = input_int("Select weight of progression", legal = (lambda x: x > 0))

    print("Parsing the files...\n")

    update_dict( pattern_dict , weight )    

    prog_len = input_int("Choose number of chords in the progression", legal = (lambda x: x >= weight))

    print("Generating progression...\n")

    try:
        the_progression = generate_prgsn(pattern_dict, weight, prog_len, True)
    except IndexError:
        the_progression  = None
   
    print("Progression generated successfully!\n")
    
    p = build_class(the_progression)   
    
    k = FileContents(title = 'hello', progression = p)
   
    with open('testxml.xml', 'w') as the_file:
        the_file.write(k.the_xml())
    
    print('Done.')
    



