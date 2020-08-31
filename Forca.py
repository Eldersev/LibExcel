import  os

class forca:
    def __init__(self, secret_word, tips):
        self.secret_word = secret_word.upper()
        self.secret_word_size = len (secret_word)
        self.secret_word_found = ('_'*len(self.secret_word))
        self.tips = tips
        self.error_count = 0
        self.try_quantity = len(self.secret_word) + 3
        self.win = False
    
    def set_letter(self,pos,letter):
        x = 0
        y = 0
        aux = ''

        while (x < len(self.secret_word)):
            if x == pos[y]:
                aux = aux + letter.upper()
                if (y < len(pos)-1): y = y+1
            else:
                aux = aux + self.secret_word_found[x].upper()
            x = x + 1
        self.secret_word_found = aux 
        if self.secret_word_found==self.secret_word:
            self.win  = True 


    def find_letter (self, letter):
        x =  0
        pos =[]
        while (x < self.secret_word_size):      
            #print( word_secret[x].lower())  
            if letter.upper() == self.secret_word[x]:
                pos.append(x)
                
            x = x+1

        if len(pos) == 0:
            self.error_count = self.error_count + 1
        else:
            self.set_letter(pos,letter)

        self.try_quantity= self.try_quantity -1
        
        return pos  
    
    def can_try (self):
        if self.try_quantity > 0 and self.error_count <2 and self.win == False:
            ret = True
        else: 
            ret = False

        return ret 

    def draw(self):
        os.system('cls')
        print ('')
        print ('') 
        print ('')
        print ('                  -------------------------')
        print ('                  |                       |')
        print ('                  |                       |')   
        if self.error_count > 2:
            print ('                  |               Perdeu a cabeça')
        else:
            print ('                  |                      ( )')

        if self.error_count > 1:
            print ('                  |               Perdeu os braços')
        else:
            print ('                  |                      /|\ ')
        print ('                  |                       | ')
        if self.error_count > 0:
            print ('                  |               Perdeu as pernas')
        print ('                  |                      / \ ')
        print ('                  |                       ')
        print ('                  |                       ')
        print ('                 / \                      ')
        print ('')
        print ('')
        if self.error_count > 2:
            print ('Você perdeu! Tente novamente')
            print ('')
            print ('')
            #try_count = len(secret_word) + 3
        elif self.win == True:
            print ('Você Ganhou! Parabens')
            print ('')
            print ('')
        elif self.can_try() == False:
            print ('Você Perdeu! Você usou todas as tentativas ')
            print ('')
            print ('')
        else:  
            print ('')
            print ('')
            print ('                            ' + self.secret_word_found) 
            print ('')
            print ('')
            print ('A dica é: ', self.tips[0] ) 
            if self.error_count > 0:
                print ('A segunda dica é: ', self.tips[1] ) 
            print ('')
            print ('')