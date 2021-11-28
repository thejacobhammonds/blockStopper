import random


chords = [['C', 'dm', 'em', 'F', 'G', 'am'],
          ['Db', 'ebm', 'fm', 'Gb', 'Ab', 'bbm'],
          ['D', 'em', 'f#m', 'G', 'A', 'bm'],
          ['Eb', 'fm', 'gm', 'Ab', 'Bb', 'cm'],
          ['E', 'f#m', 'g#m', 'A', 'B', 'c#m'],
          ['F', 'gm', 'am', 'Bb', 'C', 'dm'],
          ['Gb', 'abm', 'bbm', 'Cb', 'Db', 'eb'],
          ['G', 'am', 'bm', 'C', 'D', 'em'],
          ['Ab', 'bbm', 'cm', 'Db', 'Eb', 'Fm'],
          ['A', 'bm', 'c#m', 'D', 'E', 'f#m'],
          ['Bb', 'cm', 'dm', 'Eb', 'F', 'gm'],
          ['B', 'c#m', 'd#m', 'E', 'F#', 'g#m'],]

genKey = (chords[random.randint(0, len(chords) - 1)])





chordProg = [[1, 3, 4, 5],
             [1, 3, 6, 5],
             [1, 4, 5, 1],
             [1, 4, 6, 5],
             [1, 4, 1, 5],
             [1, 5, 6, 4],
             [1, 6, 4, 1],
             [1, 6, 4, 5],
             [1, 6, 2, 5],
             [2, 2, 5, 5],
             [2, 5, 1, 6],
             [2, 4, 1, 5],
             [2, 1, 6, 5],
             [2, 3, 4, 5],
             [4, 1, 5, 1],
             [4, 1, 5, 6],
             [4, 1, 6, 5],
             [4, 3, 6, 6],
             [4, 3, 6, 2],
             [4, 5, 6, 6],
             [5, 4, 5, 4],
             [5, 4, 1, 1],
             [5, 6, 4, 1],
             [5, 6, 4, 4],
             [6, 4, 1, 5],
             [6, 1, 4, 3],
             [6, 5, 6, 5],
             [6, 5, 4, 3],
             [6, 5, 4, 5],
             [6, 1, 4, 5],]




genChordProg = (chordProg[random.randint(0, len(chordProg) -1)])
print('key:', end= ' ')
print(genKey[0])

print('Chord Progression:')
print (genChordProg)

#loop through numbers to get chords


for i in genChordProg:
    print('|' + genKey[int(i - 1)], end= '|') 
