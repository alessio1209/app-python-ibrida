from fastapi import FastAPI #libreria principale per creare l'infrastruttura del server web
from fastapi.responses import FileResponse #importiamo questo strumento per permette a python di prendere un file fisico (il nostro html) e spedirlo al browser del client
import secrets #libreria di python per generare numeri o stringhe crittografate

app = FastAPI(title="IoT Textile Monitor") #inizializziamo la nostra applicazione. Questa variabile app è il cuore del nostro server

@app.get("/") #dice al server che quando un utente si collega all'indirizzo principale del sito (la root /), esegui la funzione che è sotto
def serve_frontend(): #funzione che gestisce la richiesta iniziale
	return FileResponse("index.html") #il server risponde prendendo il file dell'interfaccia grafica 

@app.get("/api/telai") #creiamo un nuovo indirizzo (Endpoint API). Questo non dà una pagina visiva, ma dà dati che il frontend leggerà 
def get_dati_telai(): #funzione che calcola i dati in tempo reale
	efficienza = secrets.choice(range(75,101)) 
	temperatura = secrets.choice(range(60,91))
	#se la temperatura supera gli 85 gradi, mandiamo un allert
	stato = "ALLARME TEMPERATURA" if temperatura > 85 else "ATTIVO"
	#restituiamo un dizionario (che FastAPI trasformerà in automatico in un perfetto JSON)
	return {
		"reparto": "Tessitura Prato Est",
		"stato_generale": stato, 
		"efficienza_percentuale": efficienza,
		"temperatura_media_C": temperatura,
		"telai_connessi": 42
	}


