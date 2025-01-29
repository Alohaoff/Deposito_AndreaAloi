età = int(input("Quanti anni hai? "))
lista_film = ["The Avengers: Civil War", "Pulp Fiction", "Harry Potter e l'Ordine della Fenice" ]
if età >=18:
    print(lista_film)
    film = int(input("Scegli il film da vedere: 1, 2 o 3?"))
    if film == 1:
        print("Hai scelto di vedere:" + lista_film[0])
    elif film == 2:
        print("Hai scelto di vedere:" + lista_film[1])
    elif film == 3:
        print("Hai scelto di vedere:" + lista_film[2])
    else:
        print("La scelta non è valida, ci dispiace.")
else:
    print("Ci dispiace, non puoi vedere questi film.")
    



    

    