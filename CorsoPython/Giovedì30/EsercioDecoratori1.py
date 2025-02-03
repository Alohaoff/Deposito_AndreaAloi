while True:
    scelta_entrata = input("Vuoi entrare nel menu: ").strip().lower()
    if scelta_entrata == "si":
        break
    else:
        print("Uscita dal programma")

lista_risultati = []

def risultati(funzione):
        def wrapper(*args, **kwargs):
            area = funzione(*args, **kwargs)
            lista_risultati.append(area)
            print("L'area è :", area)
            return area
        return wrapper

@risultati
def triangolo(base, altezza):
    return (base * altezza) / 2

@risultati
def quadrato(lato):
    return lato ** 2

@risultati
def rettangolo(base, altezza):
    return base * altezza


while True:
    print("\nMenu:")
    print("Tutti i risultati vengono salvati.")
    print("1- Calcola l'area di un triangolo")
    print("2- Calcola l'area di un quadrato")
    print("3- Calcola l'area di un rettangolo")
    print("4- Mostra i risultati salvati")
    print("5- Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        base = float(input("Inserisci il valore della base del triangolo: "))
        altezza = float(input("Inserisci il valore dell'altezza del triangolo: "))
        triangolo(base, altezza)

    elif scelta == "2":
        lato = float(input("Inserisci il valore del lato del quadrato: "))
        quadrato(lato)

    elif scelta == "3":
        base = float(input("Inserisci il valore della base del rettangolo: "))
        altezza = float(input("Inserisci il valore dell'altezza del rettangolo: "))
        rettangolo(base, altezza)

    elif scelta == "4":
        print("Risultati salvati:", lista_risultati)

    elif scelta == "5":
        print("Uscita dal programma")
        break

    else:
        print("Scelta non valida, riprova.")