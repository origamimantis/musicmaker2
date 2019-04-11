import xml.etree.ElementTree as et



OCTAVES = {"A" : (1,5),
           "B" : (),
           "C" : (),
           "D" : (),
           "E" : (),
           "F" : (),
           "G" : ()}

ALTER = { "b" : -1, "#" : 1}


class Progression:
    def __init__(self, the_progression : [frozenset]):
        self.length = len(the_progression)
        self.first = Chord(the_progression[0])

        tmp = self.first
        for chdnum in range(1, self.length):
            tmp.next = Chord(the_progression[chdnum])
            tmp = tmp.next
            

class Chord:
    def __init__(self, chd: frozenset):
        self.next = None
        self.notes = set(chd)


class FileContents:
    def __init__(self, title):
        self.body = et.Element('score-partwise')

        tmp1 = et.SubElement(self.body, 'work')
        tmp2 = et.SubElement(tmp1, 'work-title')
        tmp2.text = title

        tmp1 = et.SubElement(self.body, 'identification')
        tmp2 = et.SubElement(tmp1, 'creator')
        tmp2.set('type', 'composer')
        tmp2.text = 'Composer'

        tmp2 = et.SubElement(tmp1, 'encoding')
        tmp3 = et.SubElement(tmp2, 'software')
        tmp3.text = "MusicMaker v2"
        
        tmp3 = et.SubElement(tmp2, 'encoding-date')
        tmp3.text = "REEEEEEEEEEEEEEEE"

        tmp3 = et.SubElement(tmp2, 'supports')
        tmp3.set('element', 'accidental')
        tmp3.set('type', 'yes')

        tmp3 = et.SubElement(tmp2, 'supports')
        tmp3.set('element', 'beam')
        tmp3.set('type', 'yes')

        tmp3 = et.SubElement(tmp2, 'supports')
        tmp3.set('element', 'print')
        tmp3.set('attribute', 'new-page')
        tmp3.set('type', 'yes')
        tmp3.set('value', 'yes')

        tmp3 = et.SubElement(tmp2, 'supports')
        tmp3.set('element', 'print')
        tmp3.set('attribute', 'new-system')
        tmp3.set('type', 'yes')
        tmp3.set('value', 'yes')

        tmp3 = et.SubElement(tmp2, 'supports')
        tmp3.set('element', 'stem')
        tmp3.set('type', 'yes')




i = FileContents('hello').body
print(et.tostring(i))





'''  
<note>
  <chord/>
  <pitch>
    <step>E</step>
    <alter>-1</alter>
    <octave>4</octave>
  </pitch>
  <duration>1</duration>
  <voice>1</voice>
  <type>eighth</type>
  <stem>up</stem>
  <staff>1</staff>
</note>
'''

# a note is defined as a letter followed optionally by # or b.
# ^[A-G](#|b)?$

def build_class(the_p):
    prog = Progression(the_p)
    return prog
def header():
    return "--HEADER--"

def to_mxml( the_p:[] ):
    
    DESTINATION = 'out.xml'
    
    with open(DESTINATION , 'w') as the_file:
        the_file.write(header())
        for chd in the_p:
            for note in chd:
                pass