nome = ""
età = 0
cap = 0
boolRif = False

if nome =="" and età == 0 and cap == 0 and boolRif == False:
    nome =input("Inserisci il nome:")
    if nome !="" and età == 0 and cap == 0 and boolRif == False:
        età = int(input("Inserisci l'età:"))
        if nome !="" and età > 0 and cap == 0 and boolRif == False:
            cap = int(input("Inserisci il cap:"))
            if nome !="" and età == 0 and cap != 0 and boolRif == False:
                #boolRif = True
                
                riferimento = int(input("inserisci 1 o 0"))
                if (riferimento > 0):
                    boolRif = False
#completare