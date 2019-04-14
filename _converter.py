import datetime
import xml.etree.ElementTree as et

# _converter.py - this module handles encoding a chord progression into an xml file.

OCTAVES = {"A" : (1,5),
           "B" : (),
           "C" : (),
           "D" : (),
           "E" : (),
           "F" : (),
           "G" : ()}

ALTER = { "b" : '-1', "#" : '1'}


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
    def __init__(self, title, progression):
        self.body = et.Element('score-partwise')
        self.title = title

        self._work()
        self._identification()
        self._credit()
        self._partlist()
        subpart = self._add_part(True)
        curr = progression.first
        meas = 1
        while curr is not None:

            self._add_chords(meas, curr, subpart, True)
            meas += 1
            curr = curr.next


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
        tmp3.text = str(datetime.date.today())

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

    def _partlist(self):

        tmp1 = et.SubElement(self.body, 'part-list')
        
        tmp2 = et.SubElement(tmp1, 'score-part')
        tmp2.set('id', 'P1')
        
        et.SubElement(tmp2, 'part-name').text = 'Piano'
        et.SubElement(tmp2, 'part-abbreviation').text = 'Pno.'
        
        tmp3 = et.SubElement(tmp2, 'score-instrument')
        tmp3.set('id', 'P1-I1')
        et.SubElement(tmp3, 'instrument-name').text = 'Piano'

        tmp3 = et.SubElement(tmp2, 'midi-device')
        tmp3.set('id', 'P1-I1')
        tmp3.set('port','1')
        
        tmp3 = et.SubElement(tmp2, 'midi-instrument')
        tmp3.set('id', 'P1-I1')
        
        et.SubElement(tmp3, 'midi-channel').text = '1'
        et.SubElement(tmp3, 'midi-program').text = '1'
        et.SubElement(tmp3, 'volume').text = '78.7402'
        et.SubElement(tmp3, 'pan').text = '0'

    def _meas_header(self, uptree, is_chord):
        tmp3 = et.SubElement(uptree, 'print')
        tmp4 = et.SubElement(tmp3, 'system-layout')
        tmp5 = et.SubElement(tmp4, 'system-margins')
        et.SubElement(tmp5, 'left-margin').text = '0.00'
        et.SubElement(tmp5, 'right-margin').text = '0.00'
        et.SubElement(tmp4, 'top-system-distance').text = '170.00'

        tmp3 = et.SubElement(uptree, 'attributes')
        et.SubElement(tmp3, 'divisions').text = '1'

        tmp4 = et.SubElement(tmp3, 'key')
        et.SubElement(tmp4, 'fifths').text = '0'

        tmp4 = et.SubElement(tmp3, 'time')
        et.SubElement(tmp4, 'beats').text = '4'
        et.SubElement(tmp4, 'beat-type').text = '4'

        tmp4 = et.SubElement(tmp3, 'clef')
        et.SubElement(tmp4, 'sign').text = 'G' if is_chord else 'F'
        et.SubElement(tmp4, 'line').text = '2' if is_chord else '4'

    def _add_part(self, is_chord):

        tmp1 = et.SubElement(self.body, 'part')
        tmp1.set('id', 'P1' if is_chord else 'P2')
        return tmp1


    def _add_chords(self, measnum:int, chd, uptree, is_chord:bool):

        tmp2 = et.SubElement(uptree, 'measure')
        tmp2.set('number' , str(measnum))
        tmp2.set('width' , '320')
        if measnum == 1: self._meas_header(tmp2, is_chord)  
        

        self._add_notes(chd, tmp2)


    def _add_notes(self, chd, up):
        objchd = False
        
        for note in chd.notes:
            tmp3 = et.SubElement(up, 'note')
            if objchd:
                h = et.SubElement(tmp3, 'chord')
         
                
            objchd = True
            
            tmp4 = et.SubElement(tmp3, 'pitch')
          
            et.SubElement(tmp4, 'step').text = note[0]
           
            if len(note) == 2:
                et.SubElement(tmp4, 'alter').text = ALTER[note[1]]
            
            et.SubElement(tmp4, 'octave').text = '5'
            
            et.SubElement(tmp3, 'duration').text = '2'
            et.SubElement(tmp3, 'voice').text = '1'
            et.SubElement(tmp3, 'type').text = 'half'
                
                




    def the_xml(self):
        return '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">' + '>\n<'.join(et.tostring(self.body).decode().split('><'))






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
