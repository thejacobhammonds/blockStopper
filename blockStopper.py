
# This Program chooses a Key signature and Style to help jumpstart the writing process


import random
import sys


# The module randomly chooses a Key
def keyMod():
    keys = ['C major',
            'Db major',
            'D major',
            'Eb major',
            'E major',
            'F major',
            'Gb major',
            'G major',
            'Ab major',
            'A major',
            'Bb Major',
            'B Major',
            'C minor',
            'C# minor',
            'D minor',
            'Eb minor',
            'E minor',
            'F minor',
            'F# minor',
            'G minor',
            'G# minor',
            'A minor',
            'Bb minor',
            'B minor',]

    print("Key:")
    print(keys[random.randint(0, len(keys) - 1)])



# this module chooses the style

def styleMod():
    style = ['Hip Hop 85 - 95 bpm',
             'Slow Funk 95 - 100 bpm',
             'Funk 100 - 110 bpm',
             'House 110 - 120 bpm',
             'Trap 120 - 130 bpm (half time)',
             'Fast Trap 130 - 160 (half time)',
             'Bounce 160 - 180 bpm (half time)',
             "80's rock 150 - 160 bpm",
             ]
    print("Style:")
    print(style[random.randint(0, len(style) - 1)])


# this module chooses a random tempo

def tempoMod():
    tempo = random.randint(60, 180)
    print("Random Tempo:") 
    print(tempo)         

# this module chooses a chord progression

def chordMod():
    chordProg = ['/1/3/4/5/',
                 '/1/3/6/5/',
                 '/1/4/5/1/',
                 '/1/4/6/5/',
                 '/1/4/1/5/',
                 '/1/5/6/4/',
                 '/1/6/4/1/',
                 '/1/6/4/5/',
                 '/1/6/2/5/',
                 '/2/2/5/5/',
                 '/2/5/1/6/',
                 '/2/4/1/5/',
                 '/2/1/6/5/',
                 '/2/3/4/5/',
                 '/4/1/5/1/',
                 '/4/1/5/6/',
                 '/4/1/6/5/',
                 '/4/3/6/6/',
                 '/4/3/6/2/',
                 '/4/5/6/6/',
                 '/5/4/5/4/',
                 '/5/4/1/1/',
                 '/5/6/4/1/',
                 '/5/6/4/4/',
                 '/6/4/1/5/',
                 '/6/1/4/3/',
                 '/6/5/6/5/',
                 '/6/5/4/3/',
                 '/6/5/4/5/',
                 '/6/1/4/5/',]

    print('Chord Progression:')
    print(chordProg[random.randint(0, len(chordProg) -1)])




# The module randomly chooses a Key (only major)
def majKeyMod():
    keys = ['C major',
            'Db major',
            'D major',
            'Eb major',
            'E major',
            'F major',
            'Gb major',
            'G major',
            'Ab major',
            'A major',
            'Bb Major',
            'B Major',]
          

    print("Key:")
    print(keys[random.randint(0, len(keys) - 1)])





# this module prints the chord matrix

def matrixMod():
    print('''

         1    2    3    4    5    6    7 
    C:   C    Dm   Em   F    G    Am   Bdim
    
    Db:  Db   Ebm  Fm   Gb   Ab   Bbm  Cdim
    
    D:   D    Em   F#m  G    A    Bm   C#dim
    
    Eb:  Eb   Fm   Gm   Ab   Bb   Cm   Ddim
    
    E:   E    F#m  G#m  A    B    C#m  D#dim
    
    F:   F    Gm   Am   Bb   C    Dm   Edim
    
    Gb:  Gb   Abm  Bbm  Cb   Db   Ebm  Fdim
    
    G:   G    Am   Bm   C    D    Em   F#dim
    
    Ab:  Ab   Bbm  Cm   Db   Eb   Fm   Gdim
    
    A:   A    Bm   C#m  D    E    F#m  G#dim
    
    Bb:  Bb   Cm   Dm   Eb   F    Gm   Adim
    
    B:   B    C#m  D#m  E    F#   G#m  A#dim
         1    2    3    4    5    6    7
    ''')


# this module prints the circle of fifths

def circleMod():
    print("""
          /     C        \ 
         /      Am        \
             
       /F/Dm/          \Em\G\  
      
     /Bb/Gm/              \Bm\D\ 

    |Eb|Cm|                |F#m|A|

     \Ab\Fm              /C#m/E/

       \Db\Bbm\       /G#m/B/

        \        Ebm      /
         \       Gb      /
               



    """)
    

print('Hello and Welcome To Songwriter Block Stopper!')
# this randomly generates a title font


titles = [
    '''
    
    <-.(`-')                           <-.(`-') (`-').-(`-')               _  (`-')_  (`-')(`-')  _  (`-')  
     __( OO)   <-.       .->   _        __( OO) ( OO)_ ( OO).->      .->   \-.(OO )\-.(OO )( OO).-<-.(OO )  
    '-'---.\ ,--. ) (`-')----. \-,-----'-'. ,--(_)--\_)/    '._ (`-')----. _.'    \_.'    (,------,------,) 
    | .-. (/ |  (`-'( OO).-.  ' |  .--.|  .'   /    _ /|'--...__( OO).-.  (_...--'(_...--''|  .---|   /`. ' 
    | '-' `.)|  |OO ( _) | |  |/_) (`-'|      /\_..`--.`--.  .--( _) | |  |  |_.' |  |_.' (|  '--.|  |_.' | 
    | /`'.  (|  '__ |\|  |)|  |||  |OO |  .   '.-._)   \  |  |   \|  |)|  |  .___.|  .___.'|  .--'|  .   .' 
    | '--'  /|     |' '  '-'  (_'  '--'|  |\   \       /  |  |    '  '-'  |  |    |  |     |  `---|  |\  \  
    `------' `-----'   `-----'   `-----`--' '--'`-----'   `--'     `-----'`--'    `--'     `------`--' '--' 
        
 
    ''',

    '''
    
                                                                          
    ,-----. ,--.          ,--.    ,---.  ,--.                                 
    |  |) /_|  |,---. ,---|  |,-.'   .-,-'  '-.,---. ,---. ,---. ,---.,--.--. 
    |  .-.  |  | .-. | .--|     /`.  `-'-.  .-| .-. | .-. | .-. | .-. |  .--' 
    |  '--' |  ' '-' \ `--|  \  \.-'    ||  | ' '-' | '-' | '-' \   --|  |    
    `------'`--'`---' `---`--'`--`-----' `--'  `---'|  |-'|  |-' `----`--'    
                                                    `--'  `--'                


    ''',



    
    '''
    
       ____     _       U  ___ u   ____   _  __   ____     _____   U  ___ u  ____     ____   U _____ u   ____     
    U | __")u  |"|       \/"_ \/U /"___| |"|/ /  / __"| u |_ " _|   \/"_ \/U|  _"\ uU|  _"\ u\| ___"|/U |  _"\ u  
     \|  _ \/U | | u     | | | |\| | u   | ' /  <\___ \/    | |     | | | |\| |_) |/\| |_) |/ |  _|"   \| |_) |/  
      | |_) | \| |/__.-,_| |_| | | |/__U/| . \\u u___) | /| |\.-,_| |_| | |  __/   |  __/   | |___    |  _ <    
      |____/   |_____|\_)-\___/   \____| |_|\_\  |____/>> u |_|U \_)-\___/  |_|      |_|      |_____|   |_| \_\   
     _|| \\_   //  \\      \\    _// \\,-,>> \\,-.)(  (__)_// \\_     \\    ||>>_    ||>>_    <<   >>   //   \\_  
    (__) (__) (_")("_)    (__)  (__)(__)\.)   (_/(__)    (__) (__)   (__)  (__)__)  (__)__)  (__) (__) (__)  (__) 
    ''',
    ''' 
      ____  _            _     _____ _                              
    |  _ \| |          | |   / ____| |                             
    | |_) | | ___   ___| | _| (___ | |_ ___  _ __  _ __   ___ _ __ 
    |  _ <| |/ _ \ / __| |/ /\___ \| __/ _ \| '_ \| '_ \ / _ \ '__|
    | |_) | | (_) | (__|   < ____) | || (_) | |_) | |_) |  __/ |   
    |____/|_|\___/ \___|_|\_\_____/ \__\___/| .__/| .__/ \___|_|   
                                            | |   | |              
                                            |_|   |_|              
    ''',]

print(titles[random.randint(0, len(titles) - 1)])




while True:
    print(' ')
    print('Please select from the following options:')
    print('1 Choose a random key')
    print('2 Choose a random style')
    print('3 Choose a random tempo')
    print('4 Choose a random Numeric Chord progression')
    print('5 Choose a Random Key, Tempo and Chord progression')
    print('6 Show Chord matrix')
    print('7 Show Circle of Fifths')
    print('8 exit')
    response = input()

    if response == '1':
        print('')
        print('')
        keyMod()
        print('')
    if response == '2':
        print('')
        print('')
        styleMod()
        print('')
    if response == '3':
        print('')
        print('')
        tempoMod()
        print('')
    if response == '4':
        print('')
        print('')
        chordMod()
        print('')
    if response == '5':
        print('')
        print('')
        tempoMod()
        print('')
        majKeyMod()
        print('')
        chordMod()
        print('')
    if response == '6':
        print('')
        matrixMod()
        print('')
    if response == '7':
        print('')
        circleMod()
    if response == '8':
        sys.exit()
        
             
         
