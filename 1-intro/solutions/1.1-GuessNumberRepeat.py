import random

'''
Chiedi all'utente se vuole ripetere la partita quando ha finito il numero di tentativi massimi.
Richiede conoscenza del while()
'''

ripeti = "y"
while(ripeti=="y""):
    numero_random = random.randrange(1, 10)
    for tentativo in 1, 2, 3, 4, 5:
        print ('tentativo numero ' + str(tentativo))

        striga_inserita = input('inserisci il numero ')
        numero_inserito = int(striga_inserita)

        if numero_random == numero_inserito:
            print ('indovinato!\n')
            break
        else:
            print('sbagliato, riprova...\n')

    scelta = input("Vuoi fare un'altra partita ? (y,n) ")
