Coding Challenge - Backend Developer

L'obiettivo di questo challenge è implementare delle API REST per la creazione e il recupero degli utenti.
Configurare il file serverless.yml per gestire la configurazione e la creazione delle risorse nell'ambiente AWS.
Eseguire il deployment del pacchetto su AWS testando le API con Postman, verificando il corretto funzionamento delle richieste di tipo GET e POST.

[Installazione]

Per iniziare, ho configurato l'ambiente di sviluppo necessario per completare il challenge. Ho installato i seguenti pacchetti utilizzando npm:

```
npm i serverless
npm install serverless-wsgi --save-dev
npm install serverless-python-requirements --save-dev
```

Successivamente, ho installato Flask per facilitare la creazione delle API REST all'interno del file app.py.

```
pip install flask
```

Dopo aver effettuato il login con il comando `serverless login`, ho creato un nuovo progetto con il comando `serverless` e l'ho collegato al mio account AWS con `aws configure`. 


[Funzionalità]

Nel file app.py ho implementato due funzioni:

- get_user_by_id (recupero utente):
    Method : GET
    Success Response: 200
    Error Response: 404
    Questa funzione permette di recuperare un utente specifico in base all'ID passato come parametro. Se l'utente esiste nel database, viene restituito; in caso contrario, la risposta conterrà un messaggio indicante che l'utente non è stato trovato.

- create_user (creazione utente) 
    Method : POST
    Esempio Body: { 'name': 'Gianmarco Oliviero' } 
    Success Response: 200
    Error Response: 400
    Questa funzione consente di creare un nuovo utente, generando un ID univoco utilizzando la libreria uuid. Una volta generato l'ID, l'utente viene inserito nel database.