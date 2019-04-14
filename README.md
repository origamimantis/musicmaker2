# musicmaker2
musicmaker: the sequel

The main program: sequel.py

To add custom chords: place files in to_convert/ and run format_progression.py
                      make sure they contain chords of the form (note)(type), where
                      type is one of maj7, 7, -7, -7b5 (others will be added, hopefully),
                      and different chords separated by at least one space and at most one ','(comma).


generates chord progressions by generating a random chord based on the n previous chords in the progression.

Possible updates: make n variable; eg changes within a range while the program is running.
