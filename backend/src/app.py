from flask import Flask, request, jsonify
from src.Game import Game, Spielstatus
from src.UtilClasses import Spieler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

spiele = {}

@app.route('/spiel_erstellen', methods=['POST'])
def spiel_erstellen():
    spiel_name = request.json.get('name')
    if not spiel_name:
        return jsonify({'message': 'Spielname fehlt!'}), 400

    if spiel_name in spiele:
        return jsonify({'message': f'Spiel mit dem Namen {spiel_name} existiert bereits!'}), 400

    spiele[spiel_name] = Game()  # Ein neues Spielobjekt erstellen und im Dictionary speichern
    return jsonify({'message': f'Spiel {spiel_name} erstellt!'})

@app.route('/spiele', methods=['GET'])
def alle_spiele():
    return jsonify({'spiele': list(spiele.keys())})

@app.route('/spiel_loeschen', methods=['DELETE'])
def spiel_loeschen():
    spiel_name = request.json.get('name')
    if not spiel_name:
        return jsonify({'message': 'Spielname fehlt!'}), 400

    if spiel_name not in spiele:
        return jsonify({'message': f'Spiel {spiel_name} nicht gefunden!'}), 404

    del spiele[spiel_name]  # Spiel aus dem Dictionary entfernen
    return jsonify({'message': f'Spiel {spiel_name} gelöscht!'})

@app.route('/spieler_beitreten', methods=['POST'])
def spieler_beitreten():
    spieler_name = request.json.get('name')
    spiel_name = request.json.get('spiel_name')
    if not spieler_name or not spiel_name:
        return jsonify({'message': 'Name oder Spielname fehlt!'}), 400

    spiel = spiele.get(spiel_name)
    if not spiel:
        return jsonify({'message': f'Spiel {spiel_name} nicht gefunden!'}), 404

    spieler = Spieler(spieler_name)
    ret, msg = spiel.spieler_hinzufuegen(spieler)
    if ret:
        return jsonify({'message': f'Spieler {spieler_name} hat das Spiel {spiel_name} beigetreten.'})
    else:
        return jsonify({'message': msg}), 400


@app.route('/spiel_starten', methods=['POST'])
def spiel_starten():
    spiel_name = request.json.get('spiel_name')
    if not spiel_name:
        return jsonify({'message': 'Spielname fehlt!'}), 400

    spiel = spiele.get(spiel_name)
    if not spiel:
        return jsonify({'message': f'Spiel {spiel_name} nicht gefunden!'}), 404

    ret, msg = spiel.starte_spiel()
    if ret:
        return jsonify({'message': f'Spiel {spiel_name} gestartet!'})
    else:
        return jsonify({'message': msg}), 400

@app.route('/karte_ausspielen', methods=['POST'])
def karte_ausspielen():
    spieler_name = request.json.get('name')
    karten_json = request.json.get('karten')
    spiel_name = request.json.get('spiel_name')

    if not spieler_name or not spiel_name:
        return jsonify({'message': 'Name oder Spielname fehlt!'}), 400

    spiel = spiele.get(spiel_name)
    if not spiel:
        return jsonify({'message': f'Spiel {spiel_name} nicht gefunden!'}), 404

    # Direkte Verwendung der karten_json ohne Konvertierung
    ret, msg = spiel.karten_von_spieler_ausspielen(spieler_name, karten_json)
    if ret:
        return jsonify({'message': f'{spieler_name} hat die Karten {karten_json} ausgespielt.'})
    else:
        return jsonify({'message': msg}), 400


@app.route('/spielstatus_abrufen', methods=['GET'])
def spielstatus_abrufen():
    spiel_name = request.args.get('spiel_name')
    spieler_name = request.args.get('name')
    
    if not spiel_name or not spieler_name:
        return jsonify({'message': 'Spielname oder Spielername fehlt!'}), 400

    spiel = spiele.get(spiel_name)
    if not spiel:
        return jsonify({'message': f'Spiel {spiel_name} nicht gefunden!'}), 404

    spieler_kartenanzahl = {spieler.name: len(spieler.hand) for spieler in spiel.spieler}
    
    meine_karten = next((spieler.hand for spieler in spiel.spieler if spieler.name == spieler_name), [])
    ausgelegte_karten = spiel.ausgelegte_karten

    return jsonify({
        'status': spiel.status.name,
        'ausgelegte_karten': ausgelegte_karten,
        'anzahl_spieler': len(spiel.spieler),
        'aktueller_spieler': spiel.aktueller_spieler_index,
        'spieler_kartenanzahl': spieler_kartenanzahl,
        'meine_karten': meine_karten
    })


@app.route('/spiel_ende', methods=['POST'])
def spiel_ende():
    spiel_name = request.json.get('spiel_name')
    if not spiel_name:
        return jsonify({'message': 'Spielname fehlt!'}), 400

    spiel = spiele.get(spiel_name)
    if not spiel:
        return jsonify({'message': f'Spiel {spiel_name} nicht gefunden!'}), 404

    spiel.status = Spielstatus.ENDE

    return jsonify({'message': 'Spiel beendet!'})

if __name__ == '__main__':
    app.run(debug=True)
