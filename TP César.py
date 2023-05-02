caractèresMaj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caractèresMin = "abcdefghijklmnopqrstuvwxyz"
caractèresSpeciaux1 = " !?#$%&'()*+,-./0123456789"
caractèresSpeciaux2 = ':;<=>"@[\]^_`{|}àâçéèêëîôù'
caractèresSpeciaux3 = "±¼½¾ÀÇÉçïûŒœπ←↑→↓⇔∑√∞∫≈≠≤≥"

# Chiffrage d'un caractère
def chiffrer_caractere(caractere, clef, str):
    nouveau_caractere = ''
    position = 0
    for i in range(len(str)):
        if caractere == str[i]:
            position = i
        
    nouveau_caractere = str[(position + clef) % len(str)]
    return nouveau_caractere 

# Chiffrage du
def chiffrage(message, clef):
    message_chiffre = ""
    for caractere in message:
        caractere_chiffre = ''
        if caractere in caractèresMaj:
           caractere_chiffre = chiffrer_caractere(caractere, clef, caractèresMaj)
           message_chiffre += caractere_chiffre 
        elif caractere in caractèresMin:
           caractere_chiffre = chiffrer_caractere(caractere, clef, caractèresMin)
           message_chiffre += caractere_chiffre 
        elif caractere in caractèresSpeciaux1:
           caractere_chiffre = chiffrer_caractere(caractere, clef, caractèresSpeciaux1)
           message_chiffre += caractere_chiffre 
        elif caractere in caractèresSpeciaux2:
           caractere_chiffre = chiffrer_caractere(caractere, clef, caractèresSpeciaux2)
           message_chiffre += caractere_chiffre 
        elif caractere in caractèresSpeciaux3:
           caractere_chiffre = chiffrer_caractere(caractere, clef, caractèresSpeciaux3)
           message_chiffre += caractere_chiffre
        else:
            message_chiffre += caractere
    return message_chiffre    
       
        
# Lecture d'un fichier ligne par ligne        
def lecture(clef):
    message_of_file=""
    with open(messageChiffrer, 'r') as f:
        for ligne in f:
            print(ligne,  end='')
            message_of_file+=ligne
  
    
    f.close()
    return message_of_file

def ecriture(message_chiffre):
    
    f = open('Resultat.txt','w')
    f.write(message_chiffre)
    f.close()

            
            
# Programme Principal
messageChiffrer = input("Entrez le nom du fichier à chiffrer :")
clef = eval(input("Entrez la clef :"))

message_of_file=lecture(clef)
print("")
print(chiffrage(message_of_file, clef))
ecriture(chiffrage(message_of_file, clef))






