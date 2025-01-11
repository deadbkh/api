from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable pour stocker les données
data = {"niveau": 0}

# Route pour recevoir les données de l'ESP32
@app.route('/update', methods=['POST'])
def update_data():
    global data
    data["niveau"] = request.json.get("niveau", 0)
    return jsonify({"message": "Data received"}), 200

# Route pour envoyer les données au site web
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
