from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Endpoint pour recevoir les données du capteur
@app.route('/update', methods=['POST'])
def update():
    # Récupérer les données envoyées par l'ESP32
    data = request.get_json()

    if not data or 'niveau' not in data:
        return jsonify({"error": "Invalid data"}), 400

    niveau = data['niveau']
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log des données reçues
    print(f"Niveau reçu: {niveau}, Heure: {current_time}")

    return jsonify({"message": "Données reçues", "niveau": niveau, "time": current_time}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
