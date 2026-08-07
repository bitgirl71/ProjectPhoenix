"""
Project Phoenix 1.7 - Ricotta Edition

Settima revisione del programma Python di studio.

Autrice: Anna Grazia
Data: 7 agosto 2026

Obiettivo:
Continuo a dedicarmi ai dettagli stilistici, ad apprendere lo stile Python
e ad aggiungere piccole funzionalità.

I linguaggi "classici" chiedevano soprattutto di descrivere il procedimento.
Python, invece, ti invita a descrivere l'intenzione.

Ho implementato la verifica dei palindromi per nome ed età.

Ho ricominciato a ricordare cosa siano una classe, un'istanza e un oggetto.
Con essi è tornato anche il piacere di costruire un'interfaccia grafica.

Nel frattempo ho eseguito anche il refactoring della ricetta della mitica
torta di ricotta di mia madre... e sentissi che profumino!!!

Ma il vero passo avanti di oggi è un altro.

Project Phoenix possiede finalmente una vera GUI che dialoga con le funzioni
preesistenti del programma. 

Molte di esse non stampano più direttamente i risultati, ma
restituiscono valori, diventando indipendenti dall'interfaccia che le utilizza.

È il primo vero passo verso un'applicazione in cui logica e presentazione
iniziano finalmente a percorrere strade diverse.

Infine... Oggi ho capito che una funzione non dovrebbe preoccuparsi di come mostrare 
un'informazione, ma soltanto di restituirla.

Sarà l'interfaccia a decidere come utilizzarla.
"""
import tkinter as tk

def verifica():
    nome = casella_nome.get()
    eta = casella_eta.get()

    saluto = stampa_saluto(nome)

    try:
        eta = int(eta)
    except ValueError:
        etichetta_saluto.config(
            text = "ERRORE!!!\nDevi scrivere l'età in numeri.\nPer esempio: 55"
            )
        casella_eta.focus_set()
        casella_eta.selection_range(0, tk.END)
        return    

    messaggio = commenta_eta(eta)

    testo = saluto
    testo += "\n\n"
    testo += messaggio

    etichetta_saluto.config(text=testo)

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

    #print("Benvenuta in Project Phoenix.")
    #print(f"Ciao, {nome}!")

    saluto = "Benvenuta in Project Phoenix. \n"
    saluto += f"Ciao, {nome}!"

    saluto += "\n"
    saluto += lumino(nome)

    #lumino(nome)
    
    return saluto


def commenta_eta(eta):

    messaggio = f"Hai {eta} anni.\n"
    messaggio += messaggio_eta(eta)

    return messaggio


        
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
        #print("Il tuo nome è palindromo.")
        return "Il tuo nome è palindromo."
    else:
        #print("Il tuo nome non è palindromo.")   
        return "Il tuo nome non è palindromo."




def main():

    while True:   
        nome = chiedi_nome()
        eta = chiedi_eta()

        saluto = stampa_saluto(nome)
        commenta_eta(eta)

        if not chiedi_ricomincia():
            break    

if __name__ == "__main__":

    finestra = tk.Tk()
    finestra.title("Project Phoenix")
    finestra.geometry("500x300")

    etichetta_nome = tk.Label(finestra, text="Nome")
    etichetta_nome.pack()

    casella_nome = tk.Entry(finestra)
    casella_nome.pack()

    etichetta_eta = tk.Label(finestra, text="Età")
    etichetta_eta.pack()

    casella_eta = tk.Entry(finestra)
    casella_eta.pack()

    pulsante = tk.Button(
        finestra,
        text="Verifica",
        command=verifica
    )
    pulsante.pack()

    etichetta_saluto = tk.Label(
        finestra,
        text="",
        justify="left"
    )
    etichetta_saluto.pack()


    finestra.mainloop()
#    main()