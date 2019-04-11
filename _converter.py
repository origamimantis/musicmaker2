OCTAVES = {"A" : (1,5),
           "B" : (),
           "C" : (),
           "D" : (),
           "E" : (),
           "F" : (),
           "G" : ()}

ALTER = { "b" : -1, "#" : 1}
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


def _pitch(note):
    o = "        <pitch>\n"
    for func in (_step, _alter, _octave):
        o += func(note)
    o += "        </pitch>\n"
    return o

def _mxml_obj( name , value):
    return "        <" + name + ">" + value + "</" + name + ">\n"


def _step(note):
    return "          <step>" + note[0] + "</step>\n"

def _alter(note):
    return "          <alter>" + note[1] + "</alter>\n" if len(note) == 2 else ''

def _octave(note):
    return "          <octave>" + "4" + "</octave>\n"

def _note(note):
    s = "      <note>\n        <chord/>\n"
    s += _pitch(note)
    for name, value in (('duration', '2'), ('voice', '1'), ('type','half'), ('staff','1')):
        s += _mxml_obj(name, value)

    s += "      </note>\n"
    return s








def header():
    return "--HEADER--"

def to_mxml( the_p:[] ):
    
    DESTINATION = 'out.xml'
    
    with open(DESTINATION , 'w') as the_file:
        the_file.write(header())
        for chd in the_p:
            for note in chd:
                the_file.write(_note(note))

