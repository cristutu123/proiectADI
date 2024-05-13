from flask import Flask, jsonify, request  # Importăm modulele necesare din Flask
import json  # Importăm modulul json pentru a manipula datele JSON

app = Flask(__name__)  # Inițializăm o instanță a aplicației Flask

# Încărcăm datele din fișierul JSON
with open('data/cars.json') as f:
    data = json.load(f)  # Deschidem și citim fișierul JSON, încărcând datele în variabila 'data'

@app.route('/api/', methods=['GET'])  # Definim ruta '/api/' pentru metoda GET
def get_all():
    # Această funcție returnează toate obiectele din JSON
    return jsonify(data)  # Convertim lista 'data' în JSON și o returnăm ca răspuns HTTP

@app.route('/api/cauta/title/<keyword>', methods=['GET'])  # Definim ruta '/api/cauta/title/<keyword>' pentru metoda GET
def search_by_title(keyword):
    # Această funcție caută obiecte care conțin cuvântul cheie în titlu
    # Se parcurge lista 'data' și se selectează doar obiectele unde cuvântul cheie este în numele obiectului
    filtered_data = [item for item in data if keyword.lower() in item['Name'].lower()]
    return jsonify(filtered_data)  # Returnăm datele filtrate ca răspuns JSON

@app.route('/api/title/', methods=['GET'])  # Definim ruta '/api/title/' pentru metoda GET
def get_titles():
    # Această funcție extrage și returnează doar titlurile
    titles = [item['Name'] for item in data]  # Creăm o listă nouă conținând doar numele (titlurile) din fiecare obiect
    return jsonify(titles)  # Convertim lista 'titles' în JSON și o returnăm ca răspuns HTTP

if __name__ == '__main__':
    app.run(debug=True)  # Rulăm aplicația în modul de debug, pe localhost și portul implicit 5000
