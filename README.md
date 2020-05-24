# Synesthesia

Dimensions of music
Series of chords (or rest) each with a duration of a rational fraction.  For the purposes of this model, I will constrain the notes to 3 octaves from C4 to C6 and a duration in the form in the form w/2^k with 0<=k<=4 and whole number w. Therefore, I will represent a chord as a 25-long vector where the first 24 dimensions are one-hot representing whether each note is present or not and a 25th dimension as an integer w representing a duration of d/32 measures. A rest is a chord with no note present.

Need to parse MIDI files into this representation to feed them into a bidirectional LSTM. 

Perhaps add a 26th dimension for note or rest.

## Resources
* https://towardsdatascience.com/making-music-with-machine-learning-908ff1b57636
* https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5
* http://nickkellyresearch.com/python-script-transpose-midi-files-c-minor/
* http://web.mit.edu/music21/
