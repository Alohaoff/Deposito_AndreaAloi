numero1 = int(input("Inserisci il primo numero: "))
lista_operazioni = ["+", "-", "*", "/"]
print(lista_operazioni)
operazione = input("Seleziona l'operazione da eseguire tra quelle sopra: ")
numero2 = int(input("Inserisci il secondo numero: "))

if operazione == lista_operazioni[0]:
    print(numero1 + numero2)
elif operazione == lista_operazioni[1]:
    print(numero1 - numero2)
elif operazione == lista_operazioni[2]:
    print(numero1 * numero2)
elif operazione == lista_operazioni[3] and numero2 > 0 :
    print(numero1 / numero2)
elif operazione == lista_operazioni[3] and numero2 == 0 :
    print("Operazione non valida!")
else:
    print("La selezione non è valida!")
