from music21 import converter, instrument, note, chord
notes = []

file = "mario.mid"

midi = converter.parse(file)
notes_to_parse = None

if parts: # file has instrument parts
    notes_to_parse = parts.parts[0].recurse()
else: # file has notes in a flat structure
    notes_to_parse = midi.flat.notes


for element in notes_to_parse:
	print(element)
	break
    if isinstance(element, note.Note):
        notes.append(str(element.pitch))
    elif isinstance(element, chord.Chord):
        notes.append('.'.join(str(n) for n in element.normalOrder))