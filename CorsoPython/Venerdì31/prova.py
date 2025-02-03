# ripetizione = int(input("Quante volte vuoi utilizzare il sistema? "))
# lista_numeri =[]
# lista_stringhe =[]
# lista_decimali =[]
# for x in range(ripetizione):
#     print("Puoi inserire un numero intero, una stringa o un numero decimale oppure stampare.")
#     print("1- numero intero")
#     print("2- stringa")
#     print("3- numero decimale")
#     print("4- stampa numeri interi")
#     print("5- stampa stringhe")
#     print("6- stampa decimali")
#     print("7- stampa tutto")

#     scelta = input("Inserisci un valore: ")
#     if scelta == "1":
#         numero = int(input("Inserisci un numero: "))
#         lista_numeri.append(numero)
        
#     elif scelta == "2":
#         stringa = input("Inserisci una stringa: ")
#         lista_stringhe.append(stringa)

#     elif scelta == "3":
#         decimale = float(input("Inserisci un numero: "))
#         lista_decimali.append(decimale)

#     elif scelta == "4":
#         print("Numeri:", lista_numeri)

#     elif scelta == "5":
#         print("Stringhe:", lista_stringhe)

#     elif scelta == "6":
#         print("Decimali:", lista_decimali)

#     elif scelta == "7":
#         print(lista_numeri, lista_stringhe, lista_decimali)

#     else:
#         print("Scelta non valida. Riprova.")



lista_stringhe = []
stringa_prec = ""
    
while True:
    stringa_nuova = input("Inserisci una stringa: ")
    lista_stringhe.append(stringa_nuova)
    if len(stringa_nuova) <= len(stringa_prec) and stringa_prec != "":
        break
    else:
        print(lista_stringhe)