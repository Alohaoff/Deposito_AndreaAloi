pari = 0 
numeri_pari = []

while(pari < 5):
    numero= int(input("Inserisci un numero: "))
    if (numero%2 == 0):
        print("Il numero scelto è pari")
        pari +=1
        numeri_pari.append(numero)
    else:
        print("Il numero scelto è dispari")
        
print("\nHai inserito i 5 numeri pari.")
print("Questi numeri sono pari:", numeri_pari)