"""
    Project Phoenix 1.5

    Quinta revisione del programma Python di studio.

    Autrice: Anna Grazia
    Data: 5 Agosto 2026

    Obiettivo:
    Mi dedico ai dettagli stilistici ed ad apprendere lo stile Python,
    ma anche ad aggiungere piccole funzionalità.

    I linguaggi "classici" chiedevano soprattutto di descrivere il procedimento.
    Python ti invita a descrivere l'intenzione.

    Ho finalmente implementato la verifica dei palindromi per nome ed età.

    """

def chiedi_nome():
    nome = input("Come ti chiami? ")
    return nome

def chiedi_eta():

    """
    Richiede l'età dell'utente finché non viene inserito
    un numero intero valido.

    Algoritmo:
    - chiedi l'età;
    - prova a convertirla;
    - se ci riesci, restituiscila;
    - se non ci riesci, avvisa l'utente e riprova.

    Restituisce:
        int: l'età inserita dall'utente.
    """

    while True:
        eta = input("Quanti anni hai? ")

        try:
            return int(eta)
        except ValueError:
            print("ERRORE!!! Devi scrivere l'età solo in caratteri numerici, così: 12")

    

def messaggio_eta(eta):

    if controlla_palindromo(eta):
        messaggio = "Età palindroma: sicuramente farai grandi cose in questo anno!!!"
    elif eta < 18:
        messaggio = "Cosa ci fai qui?! Esci e vai al mare!"
    elif eta < 50:
        messaggio = "Vai alla grande!"
    elif eta < 65:
        messaggio = "Chi la dura, la vince!"
    else:
        messaggio = "... e hai ancora voglia di stare davanti ad un pc?!"

    return messaggio

def controlla_palindromo(numero):

    numero_originale = numero
    numero_inverso = 0

    while numero > 0:

        resto = numero % 10

        numero_inverso = (numero_inverso * 10) + resto

        numero = numero // 10

    return numero_originale == numero_inverso

def stampa_saluto(nome):
    print("Benvenuta in Project Phoenix.")
    print(f"Ciao, {nome}!")

    lumino(nome)


def commenta_eta(eta):
    print(f"Hai {eta} anni.")
    print(messaggio_eta(eta))


        
def chiedi_ricomincia():

    while True:
        scelta = input("Vuoi ricomincare da capo? S/N ").strip().upper()
       
        if scelta not in ("S", "N"):
            print("Hai sbagliato risposta! Ritenta!!!")
        else:
            return scelta == "S"

def lumino(nome):

    palindromo = True
    ind_sx = 0

    limen = (len(nome))

    ind_dx = limen - 1

    while ind_sx < ind_dx:

        if nome[ind_sx] != nome[ind_dx]:
            palindromo = False
            break

        ind_sx += 1
        ind_dx -= 1    
    
    if palindromo:
        print("Il tuo nome è palindromo.")
    else:
        print("Il tuo nome non è palindromo.")    



def main():

    while True:   
        nome = chiedi_nome()
        eta = chiedi_eta()

        stampa_saluto(nome)
        commenta_eta(eta)

        if not chiedi_ricomincia():
            break    

if __name__ == "__main__":
    main()