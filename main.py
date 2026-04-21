from fastapi import FastAPI #motore principale del server web
from fastapi.responses import FileResponse #importiamo questa libreria per permettere al server di prendere un file fisico sul disco e spedirlo al browser
import secrets #libreria crittografata di python. La usiamo per generare numeri casuali sicuri
from datetime import datetime

 
app = FastAPI(title="IoT Textile Monitor Avanzato") #crea l'istanza principale dell'app  e le dà un nome. Questa variabile app è il vigile interno di python che deciderà a chi rispondere quando arrivano le richieste dal web
 
@app.get("/") #dice al server che quando un utente si collega alla radice del sito (senza digitare nulla dopo) esegue la funzione qui sotto
def serve_frontend():
    return FileResponse("index.html")
 
# 1. Definiamo la struttura del database dell'azienda 
struttura_azienda = {
    "tessitura": ["Telaio 1", "Telaio 2", "Telaio Jacquard"],
    "filatura": ["Filatoio Nord", "Filatoio Sud"],
    "tintoria": ["Vasca Colori 1", "Vasca Asciugatura", "Miscelatore"]
}
 
# 2. API per dire al frontend quali sono i settori e le macchine (serve per il menu laterale)
@app.get("/api/struttura") #crea una nuova rotta (o endpoint). Quando il codice JavaScript nel file HTML fa un fetch ('/api/struttura'), FastAPI prende il dizionario di prima, lo trasforma automaticamente in formato JSON e lo spedisce al browser per disegnare i bottoni del menu
def get_struttura():
    return struttura_azienda
 
# 3. API dinamica: calcola i dati specifici per il macchinario richiesto
@app.get("/api/dati/{settore}/{macchinario}") #tra le {} sono variabili di percorso. Significa che se il browser chiede /api/dati/tessitura/Telaio 1, FastAPI cattura le parole "tessitura" e "Telaio 1" e le infila dentro la funzione come argomenti
def get_dati_macchina(settore: str, macchinario: str):
    # Generazione dati random realistici
    efficienza = secrets.choice(range(60, 100))
    temperatura = secrets.choice(range(40, 95))
 
    # Logica di stato
    stato = "ALLARME TEMPERATURA" if temperatura > 85 else "ATTIVO"
    if efficienza < 65:
        stato = "MANUTENZIONE RICHIESTA"
 
    # Generatore di Log fittizi
    tipi_log = [
        "Avvio ciclo di produzione standard.",
        f"Calibrazione automatica {macchinario} completata.",
        "Rilevata lieve anomalia vibrazione asse X.",
        "Pressione fluido nei parametri nominali.",
        "ERRORE: Caduta di tensione momentanea registrata."
    ]
    # Creiamo una finta lista di log recenti
    log_recenti = []
    for _ in range(3): # Genera 3 log casuali. il trattino basso indica che non importa usare il numero del contatore, basttta che il ciclo giri tre volte
        ora_finta = f"{secrets.choice(range(8, 23)):02d}:{secrets.choice(range(0, 59)):02d}:{secrets.choice(range(0, 59)):02d}" #:02d è un tipo di formattazione, dice a python che se il numero è singolo, tipo 5, deve metterci uno zero davanti (05) così che l'orario sembra vero (es. 08:05:09)
        log_recenti.append(f"[{ora_finta}] {secrets.choice(tipi_log)}")
 
    # Risposta in JSON
    return {
        "settore": settore.capitalize(), #capitalize prende la parola tessitura e la fa diventare Tessitura, con la prima lettera in maiuscolo
        "macchinario": macchinario,
        "stato": stato,
        "efficienza": efficienza,
        "temperatura": temperatura,
        "logs": log_recenti
    }
