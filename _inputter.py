def input_int( message , legal = lambda x: True):
    while True:
        g = input(message + ": ")
        try:
            f = int(g)
            if legal(f):
                return f
            print(f"'{g}' is not a legal integer.")

        except ValueError:
            print(f"'{g}' is not a legal integer.")

def input_yn( message , default = 'y'):
    while True:
        f = f" (default = {default})" if default != None else ''
        g = input(message + " (y/n)" +  f + "? ").strip().lower()
        if g == '': g = default
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


