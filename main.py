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
            
    def printFieldHitState(self):
        if self.hatSchiff == 1:
            if self.istGetroffen == 1:
                print('[x]', end='' )
            else:
                print('[  ]', end='' ) 
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
            print('getroffen!!') 
        else:
            print('verfehlt...') 
            
    def getSchiffe(self):
        schiffe = []
        for row in self.felder:
            for f in row:
                if f.hatSchiff == 1:
                    schiffe.append(f)
        return schiffe
            
    def getSindAlleSchiffeZerstört(self):
        schiffe = self.getSchiffe()
        return all(schiff.istGetroffen == 1 for schiff in schiffe) 
        
    def printSpielBrett(self):
        for row in self.felder:
            for f in row:
                f.printFieldState()
            print() 
    
    def printSpielBrettTreffer(self):
        for row in self.felder:
            for f in row:
                f.printFieldHitState()
            print() 
  
import os
import sys

class Spiel:
    brett1:Brett
    brett2:Brett
    
    def __init__(self, size:int):
        self.brett1 = Brett(size) 
        self.brett2 = Brett(size) 
        
    def printContinue(self):
        input('press enter to continue') 
        
    def printTitle(self, title):
        print('==============================') 
        print(title) 
        print('==============================')
    
    def clear(self):
        os.system('clear')
        
    def printWin(self):
        self.printTitle('YOU WIN') 
        
    def printLoose(self):
        self.printTitle('GAME OVER') 
        
    def zugSpieler1(self):
        if self.brett1.getSindAlleSchiffeZerstört():
            print('Spieler 1: keine Schiffe... ') 
            return False
        else:
            self.clear()
            self.printTitle('Spieler 1')
            self.brett2.printSpielBrettTreffer()
            print('Spieler 1: Position für Beschuss angeben')
            row = int(input('Zeile:')) 
            column = int(input('Spalte')) 
            self.brett2.beschiessen(row, column)
            self.brett2.printSpielBrettTreffer()
            self.printContinue()
            return True
        
    def zugSpieler2(self):
        if self.brett2.getSindAlleSchiffeZerstört():
            print('Spieler 2: keine Schiffe... ') 
            return False
        else:
            self.clear() 
            self.printTitle('Spieler 2')
            self.brett1.printSpielBrettTreffer()
            print('Spieler 2: Position für Beschuss angeben')
            row = int(input('Zeile:')) 
            column = int(input('Spalte')) 
            self.brett1.beschiessen(row, column)
            self.brett1.printSpielBrettTreffer()
            self.printContinue()
            return True
        
    def start(self):
        self.brett1.schiffPlatzieren(1,1)
        self.brett1.schiffPlatzieren(2,2)
        self.brett1.schiffPlatzieren(3,1)
        self.brett2.schiffPlatzieren(1,1)
        self.brett2.schiffPlatzieren(2,2)
        self.brett2.schiffPlatzieren(3,1)
        self.brett1.printSpielBrett() 
        s1hatSchiffe = 1
        s2hatSchiffe = 1
        while s1hatSchiffe == 1 and s2hatSchiffe == 1:
            s1hatSchiffe = self.zugSpieler1()
            s2hatSchiffe = self.zugSpieler2()
        self.printContinue()
        self.clear()
        
        if s1hatSchiffe == 1:
            self.printWin()
        else:
            self.printLoose()
        self.printContinue()
        sys.exit(0) 

spiel = Spiel(4)
spiel.start()

#testfeld = Feld(1,0) 
#testfeld.printFieldState()