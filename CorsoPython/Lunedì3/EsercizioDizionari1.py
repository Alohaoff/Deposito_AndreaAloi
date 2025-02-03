lista_booleani = []
lista_numeri = []
lista_stringhe = []

dizio = {}

while True:
    verofalso = bool(input("Inserisci un booleano: "))
    numintero = int(input("Inserisci un numero intero: "))
    stringa= str(input("Inserisci una parola: "))
    
    lista_booleani.append(verofalso)
    lista_numeri.append(numintero)
    lista_stringhe.append(stringa)

    dizio["tipididato"] = [lista_booleani, lista_numeri, lista_stringhe]

    print(dizio)