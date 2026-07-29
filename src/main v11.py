"""
    Project Phoenix 1.1

    Prima review programma Python completato.

    Autrice: Anna Grazia
    Data: 21 Luglio 2026

    Obiettivo:
    Creo le prime funzioni imparando Python dopo molti anni.

    I linguaggi "classici" chiedevano soprattutto di descrivere il procedimento.
    Python ti invita a descrivere l'intenzione.
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
#            eta = int(eta)
            return int(eta)
        except ValueError:
            print("ERRORE!!! Devi scrivere l'età solo in caratteri numerici, così: 12")

    

def messaggio_eta(eta):

    if eta < 18:
        messaggio = "Cosa ci fai qui?! Esci e vai al mare!"
    elif eta < 50:
        messaggio = "Vai alla grande!"
    elif eta == 55:
        messaggio = "Età palindroma: sicuramente farai grandi cose in questo anno!!!"
    elif eta < 65:
        messaggio = "Chi la dura, la vince!"
    else:
        messaggio = "... e hai ancora voglia di stare davanti ad un pc?!"

    return messaggio

def chiedi_ricomincia():
    attesa_risposta = True
    while attesa_risposta:
        scelta = input("Vuoi ricomincare da capo? S/N ")
        risposta_non_valida = scelta != "S" and scelta != "N"
       
        if risposta_non_valida:
            print("Hai sbagliato risposta! Ritenta!!!")
        #   attesa_risposta = True          
        else:
            attesa_risposta = False
        #   attesa_risposta = scelta == "S" or scelta == "N"
        
    risposta = scelta == "S"
    return risposta

def main():

    continua = True

    while continua:
    
        nome = chiedi_nome()
        eta = chiedi_eta()
        messaggio = messaggio_eta(eta)

        print(f"Ciao, {nome}!")
        print(f"Hai {eta} anni.")
        print(messaggio)
        
        print("Benvenuta in Project Phoenix.")

        continua = chiedi_ricomincia()
        #if scelta == "N":
        #   continua = False


if __name__ == "__main__":
    main()