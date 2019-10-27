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
                
    def getFeld(self, row:int, column:int):
        feld = self.felder[row][column]
        return feld
        
    def schiffPlatzieren(self, row:int, column:int):
        feld = self.getFeld(row,column)
        feld.hatSchiff = 1
        
    def getHatSchiff(self, row:int, column:int):
        feld = self.getFeld(row,column)
        return feld.hatSchiff
    
    def beschiessen(self, row:int, column:int):
        feld = self. getFeld(row, column) 
        if feld.hatSchiff:
            feld.istGetroffen = 1
    
    def printSpielBrett(self):
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
        self.brett1.schiffPlatzieren(1,1)
        self.brett1.schiffPlatzieren(2,2)
        self.brett1.schiffPlatzieren(3,1)
        self.brett1.printSpielBrett() 
        print('Position für Beschuss angeben')
        row = input('Zeile:') 
        column = input('Spalte')
        self.brett1.beschiessen(int(row),int(column)) 
        self.brett1.printSpielBrett()

spiel = Spiel(4)
spiel.start()

#testfeld = Feld(1,0) 
#testfeld.printFieldState()