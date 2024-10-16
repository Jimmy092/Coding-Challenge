Coding Challenge - Backend Developer

L'obiettivo di questo challenge è implementare delle API REST per la creazione e il recupero degli utenti.

[Installazione]

Per iniziare, ho configurato l'ambiente di sviluppo necessario per completare il challenge. Ho installato i seguenti pacchetti utilizzando npm:

- serverless
- serverless-wsgi
- serverless-python-requirements

Successivamente, ho installato Flask per facilitare la creazione delle API REST all'interno del file app.py.

Dopo aver effettuato il login con il comando serverless login, ho creato un nuovo progetto con il comando serverless e l'ho collegato al mio account AWS. 
Ho configurato il file serverless.yml per gestire la configurazione e la creazione delle risorse nell'ambiente AWS.

Completata la fase di sviluppo, ho eseguito il deployment del pacchetto su AWS e testato le API con Postman, verificando il corretto funzionamento delle richieste di tipo GET e POST.

[Funzionalità]

Nel file app.py ho implementato due funzioni:

- get_user_by_id (recupero utente): Questa funzione permette di recuperare un utente specifico in base all'ID passato come parametro. Se l'utente esiste nel database, viene restituito; in caso contrario, la risposta conterrà un messaggio indicante che l'utente non è presente nel database.

- create_user (creazione utente): Questa funzione consente di creare un nuovo utente, generando un ID univoco utilizzando la libreria uuid. Una volta generato l'ID, l'utente viene inserito nel database.