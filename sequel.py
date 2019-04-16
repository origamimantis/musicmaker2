from collections import defaultdict
from _reader     import update_dict, generate_prgsn
from _inputter   import input_int, input_yn
from _converter  import to_mxml, build_class, FileContents

if __name__ == '__main__':
   
    pattern_dict = defaultdict(set)
    
    weight = input_int("Select weight of progression", legal = (lambda x: x > 0))

    print("Parsing the files...\n")

    update_dict( pattern_dict , weight )    

    pattern_dict = dict(pattern_dict)

    if pattern_dict == {}:
        print('No files were processed, so generating a progression is impossible.')
    
    else:
        prog_len = input_int("Choose number of chords in the progression", legal = (lambda x: x >= weight), error_msg='Number of chords must be greater than the specified weight.')

        print("Generating progression...\n")

        the_progression = generate_prgsn(pattern_dict, weight, prog_len, True)
       
        print("Progression generated successfully!")
        print("Processing data...\n")
        
        p = build_class(the_progression)   
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
        



