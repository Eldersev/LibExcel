from Forca import forca 

tips = ['É um animal','Esse animal fala']
forca = forca('papagaio',tips)

forca.draw()

while (forca.can_try() == True ):
    letter = input('Entre com a letra: ')
    letter= letter[0:1]
    forca.find_letter(letter)
    forca.draw()
    
