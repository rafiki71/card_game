class GameHandler {
    constructor() {
        this.baseURL = 'http://localhost:5000';  // Passen Sie die URL und den Port entsprechend Ihrer Konfiguration an
    }

    async spielErstellen(name) {
        return this._sendRequest('/spiel_erstellen', 'POST', { name });
    }

    async alleSpiele() {
        return this._sendRequest('/spiele', 'GET');
    }

    async spielLoeschen(name) {
        return this._sendRequest('/spiel_loeschen', 'DELETE', { name });
    }

    async spielerBeitreten(name, spiel_name) {
        return this._sendRequest('/spieler_beitreten', 'POST', { name, spiel_name });
    }

    async spielStarten(spiel_name) {
        return this._sendRequest('/spiel_starten', 'POST', { spiel_name });
    }

    async karteAusspielen(name, karten, spiel_name) {
        return this._sendRequest('/karte_ausspielen', 'POST', { name, karten, spiel_name });
    }

    async spielstatusAbrufen(spiel_name, spieler_name) {
        const url = `/spielstatus_abrufen?spiel_name=${spiel_name}&name=${spieler_name}`;
        return this._sendRequest(url, 'GET');
    }    

    async spielEnde(spiel_name) {
        return this._sendRequest('/spiel_ende', 'POST', { spiel_name });
    }

    async _sendRequest(endpoint, method, data = null) {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            }
        };

        if (data) {
            options.body = JSON.stringify(data);
        }

        try {
            const response = await fetch(this.baseURL + endpoint, options);
            const result = await response.json();

            if (!response.ok) {
                throw new Error(result.message || 'Ein Fehler ist aufgetreten');
            }

            return result;
        } catch (error) {
            console.error('Error during API call:', error);
            throw error;
        }
    }
}

export default GameHandler;
