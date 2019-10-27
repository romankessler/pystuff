#-*-coding:utf8;-*-

print('==============================') 
print('SCHIFFE VERSENKEN') 
print('==============================')

#name = input('wie ist dein name?')
#print('hoi,' + name)


class Feld:
    hatSchiff:bool
    istGetroffen:bool

    def __init__(self,hatSchiff:bool, istGetroffen:bool):
        self.hatSchiff = hatSchiff
        self.istGetroffen = istGetroffen
        
    def printFieldState(self):
        if self.hatSchiff == 1:
            if self.istGetroffen == 1:
                print('[x]', end='' )
            else:
                print('[o]', end='' ) 
        else:
            print('[  ]', end='' ) 
            

class Brett:
    felder:[[Feld]]
    
    def __init__(self, size:int):
        self.felder = [] 
        for line in range(size):
            self.felder.append([])
            for col in range(size):
                self.felder[line].append(Feld(0,0))
    
    def printSpielfeld(self):
        for row in self.felder:
            for f in row:
                f.printFieldState()
            print() 
  
class Spiel:
    brett1:Brett
    brett2:Brett
    
    def __init__(self, size:int):
        self.brett1 = Brett(size) 
        self.brett2 = Brett(size) 
        
    def start(self):
        self.brett1.printSpielfeld() 

spiel = Spiel(4)
spiel.start()

#testfeld = Feld(1,0) 
#testfeld.printFieldState()