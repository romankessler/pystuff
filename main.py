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
    felder:[Feld] 
    
    def __init__(self):
        self.felder = []
        self.felder.append(Feld(1,0))
        self.felder.append(Feld(0,0))
        self.felder.append(Feld(0,0))
        self.felder.append(Feld(0,0))
    
    def printSpielfeld(self):
        for f in self.felder:
       			f.printFieldState()
  
    
        

brett = Brett() 
brett.printSpielfeld() 

#testfeld = Feld(1,0) 
#testfeld.printFieldState()