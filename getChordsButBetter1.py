import random


chords = [['C', 'dm', 'em', 'F', 'G', 'am', 'bdim', 'Bb', 'fm', 'gm','D7', 'E7', 'edim', 'C7', 'A', 'Gsus'],
          ['Db', 'ebm', 'fm', 'Gb', 'Ab', 'bbm', 'cdim', 'B', 'gbm', 'abm', 'Eb7', 'F7', 'fdim', 'Db', 'Eb7', 'Absus'],
          ['D', 'em', 'f#m', 'G', 'A', 'bm', 'c#dim', 'C', 'gm', 'am', 'E7', 'F#7','f#dim', 'D7', 'B', 'Asus'],
          ['Eb', 'fm', 'gm', 'Ab', 'Bb', 'cm', 'ddim', 'Db', 'abm', 'bbm', 'F7', 'G7', 'gdim', 'Eb7', 'C', 'Bbsus'],
          ['E', 'f#m', 'g#m', 'A', 'B', 'c#m', 'd#dim', 'D', 'am', 'bm', 'F#7', 'G#7', 'g#dim', 'E7', 'C#', 'Bsus'],
          ['F', 'gm', 'am', 'Bb', 'C', 'dm', 'edim', 'Eb', 'bbm', 'cm', 'G7', 'A7', 'adim', 'F7', 'D', 'Csus'],
          ['Gb', 'abm', 'bbm', 'Cb', 'Db', 'ebm', 'fdim', 'E', 'cbm', 'dbm', 'Ab7', 'Bb7', 'bbdim', 'Gb7', 'Eb', 'Dbsus'],
          ['G', 'am', 'bm', 'C', 'D', 'em', 'f#dim', 'F', 'cm', 'dm', 'A7', 'B7', 'bdim', 'G7', 'E', 'Dsus'],
          ['Ab', 'bbm', 'cm', 'Db', 'Eb', 'Fm', 'gdim', 'Gb', 'dbm', 'ebm', 'Bb7', 'C7', 'cdim', 'Ab7', 'F', 'Ebsus'],
          ['A', 'bm', 'c#m', 'D', 'E', 'f#m', 'g#dim', 'G', 'dm', 'em', 'B7', 'C#7', 'c#dim', 'A7', 'F#', 'Esus'],
          ['Bb', 'cm', 'dm', 'Eb', 'F', 'gm', 'adim', 'Ab', 'ebm', 'fm', 'C7', 'D7', 'ddim', 'Bb7', 'G', 'Fsus'],
          ['B', 'c#m', 'd#m', 'E', 'F#', 'g#m', 'a#dim', 'A', 'em', 'f#m', 'C#7', 'D#7', 'd#dim', 'B', 'G#', 'F#sus'],]

genKey = (chords[random.randint(0, len(chords) - 1)])


numerals = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii', 'bVII', 'iv', 'v', 'II7', 'III7', 'iiidim', 'I7', 'VI', 'Vsus']


#  I  ii  iii  IV   V   vi  viidim bVII  iv  v    II7  III7  iiidim I7   VI  Vsus
#  1  2   3    4    5   6   7      8     9   10   11   12    13     14   15   16


chordProg = [[1, 3, 4, 5],     # | I |iii|IV | V | 
             [1, 3, 6, 5],     # | I |iii|Vi | V |
             [1, 4, 5, 1],     # | I |IV | V | I |
             [1, 4, 6, 5],     # | I |IV |vi | V |
             [1, 4, 1, 5],     # | I |IV | I | V |
             [1, 5, 6, 4],     # | I | V |vi |IV |
             [1, 6, 4, 1],     # | I |vi |IV | I |
             [1, 6, 4, 5],     # | I |vi |IV | V |
             [1, 6, 2, 5],     # | I |vi |ii | V |
             [1, 1, 4, 9],     # | I | I |IV |iv |
             [1, 11, 2, 5],    # | I |II7|ii | V |
             [1, 13, 4, 9],    # | I |iiidim|IV |iv |
             [1, 14, 4, 9],    # | I |I7 |IV |iv |
             [1, 12, 4, 5],    # | I |III7|ii | V |
             [1, 15, 2, 5],    # | I |VI7|ii |V| 
             [2, 2, 5, 5],     # |ii |ii | V | V |
             [2, 2, 3, 3],     # |ii |ii |iii|iii| 
             [2, 5, 1, 6],     # |ii | V | I |vi |
             [2, 4, 1, 5],     # |ii |IV | I | V |
             [2, 1, 6, 5],     # |ii | I |vi | V |
             [2, 3, 4, 5],     # |ii |iii|IV | V |
             [2, 5, 15, 15],   # |ii | V |VI |VI |
             [4, 1, 5, 1],     # |IV | I | V | I |
             [4, 1, 5, 6],     # |IV | I | V |vi |
             [4, 1, 6, 5],     # |IV | I |vi | V |
             [4, 3, 6, 6],     # |IV |iii|vi |vi |
             [4, 3, 6, 2],     # |IV |iii|vi |ii |
             [4, 3, 6, 11],    # |IV |iii|vi |II |
             [4, 12, 6, 10],   # |IV |III|vi |v  |
             [4, 12, 6, 10],   # |IV |III|vi |v  |
             [4, 5, 6, 6],     # |IV | V |vi |vi | 
             [4, 5, 6, 8],     # |IV | V |vi |bVII|
             [5, 4, 5, 4],     # | V |IV | V |IV |
             [5, 4, 1, 1],     # | V |IV | I | I |
             [5, 6, 4, 1],     # | V |vi |IV | I |
             [5, 6, 4, 4],     # | V |vi |IV |IV |
             [6, 4, 1, 5],     # |vi |VI | I | V |
             [6, 1, 4, 3],     # |vi | I |IV |iii|
             [6, 1, 4, 12],    # |vi | I |IV |III|
             [6, 5, 6, 5],     # |vi | V |vi | V |
             [6, 5, 4, 3],     # |vi | V |IV |iii|
             [6, 5, 4, 5],     # |vi | V |IV | V |
             [6, 1, 4, 5],     # |vi | I |IV | V |
             [6, 11, 1, 16],   # |vi |II7| I |Vsus|   
             [8, 4, 1, 1],     # |bVII|IV | I | I |
             [9, 10, 1, 1]]    # |iv | v | I | I | 




genChordProg = (chordProg[random.randint(0, len(chordProg) -1)])
print('key:', end= ' ')
print(genKey[0])


#loop through numbers to get chords
print('')
print('Chord Progression', end= ' ')
for i in genChordProg:
    print('|' + genKey[int(i - 1)], end= '|') 

print('')
print('')

print('        analysis:', end=' ')

for i in genChordProg:
    print('|' + numerals[int(i - 1)], end= '|') 
