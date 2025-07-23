# Importa la classe Flask per creare l'applicazione web e jsonify per restituire risposte JSON
from flask import Flask, jsonify
# Importa CORS per abilitare le richieste cross-origin (utile per frontend separati)
from flask_cors import CORS

# Istanzia l'applicazione Flask
app = Flask(__name__)
# Abilita CORS sull'applicazione per permettere richieste da altri domini
CORS(app)

# Definisce una route HTTP GET all'endpoint '/api/hello'
@app.route('/api/hello')
## Funzione associata alla route: restituisce un messaggio JSON
def hello():
    # Restituisce una risposta JSON con un messaggio di saluto
    return jsonify({ "message": "Hello from Python backend!" })

# Avvia l'applicazione Flask solo se il file viene eseguito direttamente
if __name__ == '__main__':
    # L'applicazione ascolta su tutte le interfacce di rete (host '0.0.0.0') e sulla porta 5000
    app.run(host='0.0.0.0', port=5000)