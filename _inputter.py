

# _inputter.py - this module contains ways to ask a user to input data.


def input_int( message:str , legal = lambda x: True, error_msg = None) -> int:
    '''Repeatedly asks user to enter an integer until they do, then returns the integer.'''
    while True:
        g = input(message + ": ")
        try:
            f = int(g)
            if legal(f):
                return f
            print(f"Entered: '{g}' | Error: not a legal integer." if error_msg is None else f"Entered: '{g}' | Error: " + error_msg + '\n')

        except ValueError:
            print(f"Entered: '{g}' | Error: not an integer.")

def input_yn( message:str , default:str = 'Yes')-> bool:
    '''Repeatedly asks user to enter 'y' or 'n' until they do, then returns bool matching their choice.'''
    while True:
        f = f" (default = {default})" if default != None else ''
        g = input(message + " (Y/N)" +  f + "? ").strip().lower()
        if g == '': g = default.strip().lower()
        if g in ('y','yes','n','no'):
            return g in ('y','yes')
        print("Invalid entry.")

 

# UNUSED -----



def input_note( legal = lambda x: True ):
    while True:
        g = input("Enter a note: ")
        if not len(g):
            return None
        elif g[0] in "ABCDEFG":
            if len(g) == 1:
                return g
            else:
                if g[1] in "#b":
                    if   len(g) == 2:
                        return g
                    elif len(g) == 3:
                        if g[2] == 't':
                            return g
                elif g[1] == 't':
                    if len(g) == 2:
                        return g

        print("That is not a valid note.")

def input_chord( message , legal = lambda x: True):
    chord = []
    print(message)

    while True:
        print("\nNotes in chord: [", ' , '.join(chord) , "]")
        g = input_note( legal )
        if g == None: 
            if len(chord):
                break
            print("A chord must contain at least one note!")
        else:
            chord.append(g)
    return "[" + ';'.join(chord) + "]"


