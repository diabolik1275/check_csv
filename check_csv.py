import csv
import os

def valida_csv(percorso_file, separatore=';', colonne_attese=24):
    if not os.path.isfile(percorso_file):
        print(f"Il file '{percorso_file}' non esiste nella cartella corrente. ('{os.getcwd()}')")
        return

    with open(percorso_file, mode='r', encoding='latin1') as csvfile:
        lettore = csv.reader(csvfile, delimiter=separatore)
        righe_errate = []
        prima_riga = next(lettore)
        print(f"Prima riga: {prima_riga} ({len(prima_riga)} colonne)")
        for indice, riga in enumerate(lettore, start=1):
            if len(riga) != colonne_attese:
                righe_errate.append((indice, len(riga), riga))
    
    if righe_errate:
        print(f"\nTrovate {len(righe_errate)} righe con un numero errato di colonne:")
        for riga in righe_errate:
            print(f"  → Riga {riga[0]}: {riga[1]} colonne invece di {colonne_attese}")
    else:
        print("\nTutte le righe hanno il numero corretto di colonne.")

if __name__ == "__main__":
    percorso = input("Inserisci il percorso del file CSV da controllare: ").strip()
    valida_csv(percorso)
