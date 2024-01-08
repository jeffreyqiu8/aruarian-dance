from cs101audio import *
bpm=100
mspb = (60*1000)/bpm
def makeRest(beats):
    return Audio(int(mspb*beats))
def addBeat(note, aud, beats):
    aud += generate_music_note(note, int(mspb*beats), "Sine")
def makeNote(note, beats):
    a = generate_music_note(note, int(mspb*beats), "Sine")
    a.apply_gain(-25)
    return a
def makeChord(notes, beats):
    a = makeNote(notes[0], beats)
    for x in range(len(notes)-1):
        a.overlay(makeNote(notes[x+1], beats))
    return a
def bassDrum(beats):
    bd = Audio()
    bd.open_audio_file("kick009.wav")
    bd.apply_gain(-20)
    if (beats * mspb) < len(bd):
        return bd[:beats*mspb]
    else:
        return bd + Audio((beats*mspb)-len(bd))
def hihat(beats):
    hh = Audio()
    hh.open_audio_file("hihat.wav")
    hh.apply_gain(-25)
    if (beats * mspb) < len(hh):
        return hh[:beats*mspb]
    else:
        return hh + Audio((beats*mspb)-len(hh))
def snare(beats):
    sn = Audio()
    sn.open_audio_file("snare.wav")
    sn.apply_gain(-30)
    if (beats * mspb) < len(sn):
        return sn[:beats*mspb]
    else:
        return sn + Audio((beats*mspb)-len(sn))
def main():
    main = Audio()
    treble = Audio()
    bass = Audio()
    bline = Audio()
    hihats = Audio()
    snares = Audio()
    #all percussion
    bline += makeRest(6*4)
    hihats += makeRest(6*4)
    snares += makeRest(6*4)
    for _ in range(12):
        #first measure
        bline += bassDrum(0.25)
        bline += bassDrum(0.25)
        bline += makeRest(2)
        bline += bassDrum(0.25)
        bline += bassDrum(0.25)
        bline += makeRest(1)
        for _ in range(12):
            snares += makeRest(1)
            snares += snare(1)
        for _ in range(8):
            hihats += hihat(0.5)
        #second measure
        bline += bassDrum(0.25)
        bline += bassDrum(0.25)
        bline += makeRest(1.25)
        bline += bassDrum(0.25)
        bline += makeRest(0.5)
        bline += bassDrum(0.25)
        bline += makeRest(1.25)
        snares += makeRest(1)
        snares += snare(0.75)
        snares += makeRest(1.25)
        snares += snare(1)
        for i in range(8):
            hihats += hihat(0.5)
    
    #m1
    treble += makeChord(["B3", "D#4", "F#4", "A#4"], 0.5)
    treble += makeNote("B3", 0.5)
    treble += makeNote("D#4", 0.5)
    treble += makeChord(["B3", "D#4", "F#4", "A#4"], 1)
    treble += makeNote("D#4", 0.5)
    treble += makeNote("B3", 0.5)
    treble += makeNote("F#3", 0.5)
    bass += makeChord(["G#2", "D#3", "F#3"], 1.5)
    bass += makeChord(["G#2", "D#3", "F#3"], 2.5)
    #m2
    treble += makeNote("F3", 1)
    treble += makeChord(["G#4", "G#5"], 1)
    treble += makeChord(["C#5", "C#6"], 1)
    treble += makeChord(["A#4", "A#5"], 1)
    bass += makeChord(["C#3", "C#2"], 4)
    #m3
    treble += makeChord(["B3", "D#4", "A#4"], 1)
    treble += makeNote("B3", 0.5)
    treble += makeNote("D#4", 0.5)
    treble += makeChord(["A#3", "C#4", "G#4"], 1)
    treble += makeNote("A#3", 0.5)
    treble += makeNote("C#4", 0.5)
    bass += makeNote("G#2", 0.5)
    bass += makeNote("F#3", 0.5)
    bass += makeRest(1)
    bass += makeNote("A#2", 0.5)
    bass += makeNote("F3", 0.5)
    bass += makeRest(1)
    #m4
    treble += makeChord(["B3", "D#4", "F#4"], 1)
    treble += makeNote("B3", 0.5)
    treble += makeNote("D#4", 0.5)
    treble += makeChord(["B3", "D4", "G#4"], 0.5)
    treble += makeNote("D#4", 0.5)
    treble += makeNote("B3", 0.5)
    treble += makeNote("F3", 0.5)
    bass += makeNote("G#2", 0.5)
    bass += makeNote("F#3", 0.5)
    bass += makeRest(1)
    bass += makeChord(["C#2", "C#3"], 2)
    #m5
    treble += makeChord(["A#3", "D#4"], 1.5)
    treble += makeChord(["A#3", "D#4"], 1)
    treble += makeNote("A#3", 1.5)
    bass += makeNote("F#2", 0.5)
    bass += makeNote("C#3", 0.5)
    bass += makeNote("G#3", 2)
    bass += makeNote("G#3", 0.5)
    bass += makeNote("C#3", 0.5)
    #m6
    treble += makeChord(["B3", "D4"], 1)
    treble += makeChord(["C#4", "C#5"], 1)
    treble += makeChord(["F#4", "F#5"], 1)
    treble += makeChord(["F4", "F5"], 1)
    bass += makeChord(["B2", "F#3"], 4)
    #m7-10
    for _ in range(4):
        treble += makeRest(1)
        treble += makeNote("A#3", 0.5)
        treble += makeNote("D#4", 1)
        treble += makeNote("A#3", 1.5)
        bass += makeNote("F#2", 0.5)
        bass += makeNote("C#3", 0.5)
        bass += makeNote("G#3", 2)
        bass += makeNote("G#3", 0.5)
        bass += makeNote("C#3", 0.5)
    #m11-14
    for _ in range(2):
        treble += makeChord(["B3", "D#4", "F#4", "A#4"], 0.5)
        treble += makeNote("B3", 0.5)
        treble += makeNote("D#4", 0.5)
        treble += makeChord(["B3", "D#4", "F#4", "A#4"], 1)
        treble += makeNote("D#4", 0.5)
        treble += makeNote("B3", 0.5)
        treble += makeNote("F#3", 0.5)
        bass += makeNote("G#2", 0.5)
        bass += makeNote("F#3", 1)
        bass += makeChord(["G#2", "F#3"], 2.5)
        #m12
        treble += makeNote("F3", 1)
        treble += makeChord(["G#4", "G#5"], 1)
        treble += makeChord(["C#5", "C#6"], 1)
        treble += makeChord(["A#4", "A#5"], 1)
        bass += makeChord(["C#3", "C#2"], 4)
    #m15
    for _ in range(2):
        treble += makeNote("B3", 0.25)
        treble += makeNote("D#4", 0.25)
        treble += makeNote("F#4", 0.25)
        treble += makeNote("A#4", 0.25)
    for _ in range(2):
        treble += makeNote("A#3", 0.25)
        treble += makeNote("C#4", 0.25)
        treble += makeNote("F4", 0.25)
        treble += makeNote("G#4", 0.25)
    bass += makeChord(["G#2", "D#3", "F#3"], 2)
    bass += makeChord(["A#2", "F3", "G#3"], 2)
    #m16
    for _ in range(2):
        treble += makeNote("G#3", 0.25)
        treble += makeNote("B3", 0.25)
        treble += makeNote("D#4", 0.25)
        treble += makeNote("F#4", 0.25)
    treble += makeNote("G#3", 0.25)
    treble += makeNote("B3", 0.25)
    treble += makeNote("D4", 0.25)
    treble += makeNote("F4", 0.25)
    treble += makeRest(0.75)
    treble += makeNote("D#4", 0.25)
    bass += makeChord(["G#2", "D#3", "F#3"], 2)
    bass += makeChord(["G2", "D#3", "F3"], 2)
    #m17
    treble += makeNote("D#5", 2)
    treble += makeNote("D#5", 0.5)
    treble += makeNote("F5", 0.5)
    treble += makeNote("F#5", 0.5)
    treble += makeNote("G#5", 0.5)
    bass += makeChord(["D#3", "G#3", "A#3"], 4)
    #m18
    treble += makeNote("A5", 1)
    treble += makeNote("A#5", 1)
    treble += makeNote("B5", 1)
    treble += makeNote("C#6", 1)
    bass += makeChord(["D#3", "G#3", "A#3"], 4)
    #m19-22
    for _ in range(4):
        treble += makeChord(["B3", "D#4", "F#4", "A#4"], 0.5)
        treble += makeNote("B3", 0.5)
        treble += makeNote("D#4", 0.5)
        treble += makeChord(["B3", "D#4", "F#4", "A#4"], 1)
        treble += makeNote("D#4", 0.5)
        treble += makeNote("B3", 0.5)
        treble += makeNote("F#3", 0.5)
        bass += makeNote("G#2", 0.5)
        bass += makeNote("F#3", 1)
        bass += makeChord(["G#2", "F#3"], 2.5)
        #m12
        treble += makeNote("F3", 1)
        treble += makeChord(["G#4", "G#5"], 1)
        treble += makeChord(["C#5", "C#6"], 1)
        treble += makeChord(["A#4", "A#5"], 1)
        bass += makeChord(["C#3", "C#2"], 4)
    #m23
    for _ in range(2):
        treble += makeNote("B3", 0.25)
        treble += makeNote("D#4", 0.25)
        treble += makeNote("F#4", 0.25)
        treble += makeNote("A#4", 0.25)
    for _ in range(2):
        treble += makeNote("A#3", 0.25)
        treble += makeNote("C#4", 0.25)
        treble += makeNote("F4", 0.25)
        treble += makeNote("G#4", 0.25)
    bass += makeChord(["G#2", "D#3", "F#3"], 2)
    bass += makeChord(["A#2", "F3", "G#3"], 2)
    #m24
    for _ in range(2):
        treble += makeNote("G#3", 0.25)
        treble += makeNote("B3", 0.25)
        treble += makeNote("D#4", 0.25)
        treble += makeNote("F#4", 0.25)
    treble += makeNote("G#3", 0.25)
    treble += makeNote("B3", 0.25)
    treble += makeNote("D4", 0.25)
    treble += makeNote("F4", 0.25)
    treble += makeRest(0.75)
    treble += makeNote("D#4", 0.25)
    bass += makeChord(["G#2", "D#3", "F#3"], 2)
    bass += makeChord(["G2", "D#3", "F3"], 2)
    #m25
    treble += makeNote("D#5", 2)
    treble += makeNote("D#5", 0.5)
    treble += makeNote("F5", 0.5)
    treble += makeNote("F#5", 0.5)
    treble += makeNote("G#5", 0.5)
    bass += makeChord(["D#3", "G#3", "A#3"], 4)
    #m26
    treble += makeNote("A5", 1)
    treble += makeNote("A#5", 1)
    treble += makeNote("B5", 1)
    treble += makeNote("C#6", 1)
    bass += makeChord(["D#3", "G#3", "A#3"], 4)
    
    
    main += bline
    main.overlay(hihats)
    main.overlay(snares)
    main.overlay(treble)
    main.overlay(bass)
    main.play()
    
if __name__ == "__main__":
    main()