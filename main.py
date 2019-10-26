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
                print('[x]')
            else:
                print('[o]') 
        else:
            print('[  ]') 
            

class Brett:
    felder:Feld[] 
    
    def __init__(self):
        self.felder = Feld[5] 
    
    def printSpielfeld(self):
        for f in self.felder
       			f.printFieldState()
  
    
        

brett = Brett() 

#testfeld = Feld(1,0) 
#testfeld.printFieldState()