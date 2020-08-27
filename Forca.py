class forca:
    def __init__(self, secret_word, tips):
        self.secret_word = secret_word.upper()
        self.secret_word_size = len (secret_word)
        self.tips = tips
        self.error_count = 0

    def find_letter (letter):
        x =  0
        pos =[]
        while (x < self.secret_word_size):      
            #print( word_secret[x].lower())  
            if letter.upper() == secret_word[x]:
                pos.append(x)
            x = x+1

        return pos  

    def draw():
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
        else:
            print ('')
            print ('')
            print ('                            ' + word_secret_string) 
            print ('')
            print ('')
            print ('A dica é: ', self.tips[0] ) 
            if self.error_count > 0:
                print ('A segunda dica é: ', self.tips[1] ) 
            print ('')
            print ('')