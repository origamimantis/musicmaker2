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
        self.title = title

        self._work()
        self._identification()


    def _work(self):
        tmp1 = et.SubElement(self.body, 'work')
        tmp2 = et.SubElement(tmp1, 'work-title')
        tmp2.text = self.title

    def _identification(self):

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

    def _defaults(self):

        tmp1 = et.SubElement(self.body, 'defaults')
        
        tmp2 = et.SubElement(tmp1, 'scaling')
        
        et.SubElement(tmp2, 'millimeters').text = '7.0556'
        
        et.SubElement(tmp2, 'tenths').text = '40'

        tmp2 = et.SubElement(tmp1, 'page-layout')
        
        et.SubElement(tmp2, 'page-height').text = '1683.36'
        et.SubElement(tmp2, 'page-width').text = '1190.88'
        
        tmp3 = et.SubElement(tmp2, 'page-margins')
        tmp3.set('type','even')
        et.SubElement(tmp3, 'left-margin').text = '56.6929'
        et.SubElement(tmp3, 'right-margin').text = '56.6929'
        et.SubElement(tmp3, 'top-margin').text = '56.6929'
        et.SubElement(tmp3, 'bottom-margin').text = '113.386'
        
        tmp3 = et.SubElement(tmp2, 'page-margins')
        tmp3.set('type','odd')
        et.SubElement(tmp3, 'left-margin').text = '56.6929'
        et.SubElement(tmp3, 'right-margin').text = '56.6929'
        et.SubElement(tmp3, 'top-margin').text = '56.6929'
        et.SubElement(tmp3, 'bottom-margin').text = '113.386'

        tmp2 = et.SubElement(tmp1, 'word-font')
        tmp2.set('font-family' , 'FreeSerif')
        tmp2.set('font-size' , '10')

        tmp2 = et.SubElement(tmp1, 'lyric-font')
        tmp2.set('font-family' , 'FreeSerif')
        tmp2.set('font-size' , '11')

    def _credit(self):

        tmp1 = et.SubElement(self.body, 'credit')
        tmp1.set('page', '1')
        
        tmp2 = et.SubElement(tmp1, 'credit-words')
        tmp2.set('default-x', '595')
        tmp2.set('default-y', '1627')
        tmp2.set('justify', 'center')
        tmp2.set('valign', 'top')
        tmp2.set('font-size', '24')
        tmp2.text = self.title
        
        tmp1 = et.SubElement(self.body, 'credit')
        tmp1.set('page', '1')
        
        tmp2 = et.SubElement(tmp1, 'credit-words')
        tmp2.set('default-x', '1134')
        tmp2.set('default-y', '1527')
        tmp2.set('justify', 'right')
        tmp2.set('valign', 'bottom')
        tmp2.set('font-size', '12')
        tmp2.text = 'Composer'


    def the_xml(self):
        return '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">'+ et.tostring(self.body).decode()

k = FileContents(title = 'hello')
with open('testxml.xml', 'w') as the_file:
    the_file.write(k.the_xml())



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
