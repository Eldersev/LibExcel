
import  os 

print ('------------------------------------------------------------------------------------------------------------------------')
print ('--------------------------------------------------- JOGO DA FORCA ------------------------------------------------------')
print ('------------------------------------------------------------------------------------------------------------------------')



def draw(secret_word_searched, error_count ):
    os.system('cls')
    print ('')
    print ('') 
    print ('')
    print ('                  -------------------------')
    print ('                  |                       |')
    print ('                  |                       |')   
    if error_count > 2:
        print ('                  |               Perdeu a cabeça')
    else:
        print ('                  |                      ( )')

    if error_count > 1:
        print ('                  |               Perdeu os braços')
    else:
        print ('                  |                      /|\ ')
    print ('                  |                       | ')
    if error_count > 0:
        print ('                  |               Perdeu as pernas')
    print ('                  |                      / \ ')
    print ('                  |                       ')
    print ('                  |                       ')
    print ('                 / \                      ')
    print ('')
    print ('')
    if error_count > 2:
        print ('Você perdeu! Tente novamente')
        print ('')
        print ('')
        try_count = len(secret_word) + 3
    else:
        print ('')
        print ('')
        print ('                            ' + word_secret_string) 
        print ('')
        print ('')
        print ('A dica é: ', tip ) 
        if error_count > 0:
            print ('A segunda dica é: ', tip2 ) 
        print ('')
        print ('')


def find_letter (letter, word_secret=''):
    word_size = len(word_secret)
    x =  0
    pos =[]
    while (x < word_size):      
        #print( word_secret[x].lower())  
        if letter.lower() == word_secret[x].lower():
            pos.append(x)
        x = x+1

    return pos  



secret_word = ''
tip = ''
tip2 = ''




os.system('cls')
choise = int( input ('Escolha um numero de 1 a 7: '))

if choise == 1:
    secret_word = 'papagaio'
    tip = 'É um animal'
    tip2 = 'Este animal voa'
elif choise ==2:
    secret_word = 'cachorro'
    tip = 'É um animal'
    tip2 = 'Este animal late'
elif choise ==3:
    secret_word = 'capitolio'
    tip = 'É um lugar que já viajamos'
    tip2 = 'Este lugar tem cachoeiras'
elif choise ==4:
    secret_word = 'escola'
    tip = 'Lugar de ensinamentos'
    tip2 = 'Local de estudos'
elif choise ==5:
    secret_word = 'casa'
    tip = 'É lugar'
    tip2 = 'Você passa a maior parte do tempo nesse local'
elif choise ==6:
    secret_word = 'vermelho'
    tip = 'É uma cor'
    tip2 = 'Essa cor é forte'
elif choise ==7:
    secret_word = 'cama'
    tip = 'Quando a gente acorda a gente ???'
    tip2 = 'Ação que devemos fazer após levantar'

word_size = len(secret_word)


x=0
word_secret_string = ''
secret_word_searched = ''
while (x < word_size):
    word_secret_string = word_secret_string + ' _' 
    secret_word_searched = secret_word_searched + '_'
    x = x+1

draw (secret_word_searched,0)

try_count = 0
try_count = len(secret_word) + 3
x = 0
error_count = 0
while (x < try_count):
    
    letter = input ('Entre com a letra: ')
    if len(letter) > 1: 
        letter = letter[0:1]
    ret = find_letter(letter[0:1], secret_word)


    y = 0 
    z = 0
    aux = ''

    if len(ret) == 0:
        error_count = error_count +1 

    while  (y< len(secret_word) and len(ret) > 0 ):
        if y == ret[z]:
            aux = aux + letter.upper()
            z = z +1 
            if z >= len(ret): 
                z = z - 1
        else: 
            aux = aux + secret_word_searched[y]
        y = y+1
    
    if len(aux) >  0:
        secret_word_searched = aux
    word_secret_string = ''
    y = 0
    while (y < word_size ):
        word_secret_string = word_secret_string + ' ' + secret_word_searched[y]
        y=y+1
        
    draw (secret_word_searched, error_count)
    x = x + 1
    
    if secret_word_searched.upper() == secret_word.upper():
        print ('VOCÊ GANHOU !!!! ')
        print ('PARABÉNS')
        print ('')
        break
        exit() 

   
