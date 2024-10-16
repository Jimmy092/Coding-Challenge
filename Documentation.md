# Coding challenge backend developer

Lo scopo del challenge è di implementare delle REST API per la creazione e il retrieval degli users.

[Installazione]
Come prima cosa ho fatto tutte le installazioni necessarie per poter avere un ambiente di sviluppo per portare a termine il challenge. Ho installato serverless, serverless-wsgi, serverless-python-requirements con npm dopodichè sono passato all' installazione di Flask da utilizzare all'interno del file app.py per facilitare la creazione delle REST API.
Una volta fatto "serverless login", con il comando "serverless" ho creato un nuovo progetto e ci ho collegato il mio account di AWS.
Ho creato il file 'serverless.yml' per la configurazione e la creazione di risorse sull'ambiente di AWS.
Una volta completata la parte di coding ho deployato il pacchetto e fatto dei test con PostMan per le request di tipo GET e POST.

[Funzionalità]
All'interno di app.py ho creato due funzioni:
- get_user_by_id (per il retrieval di un utente)
    dato un id passato come parametro della funzione, andiamo a prendere un utente se esiste. Nel caso in cui esiste, lo ritorniamo, altrimenti la risposta conterrà una stringa che indicherà che l'utente non è presente nel database.
- create_user (per la creazione di un utente)
    creiamo un utente con id generato con la libreria uuid dopodichè lo inseriamo nel database.