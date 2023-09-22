# Basierend auf einer offiziellen Python-Basisimage
FROM python:3.9-slim

# Setzt das Arbeitsverzeichnis im Docker-Container
WORKDIR /app

# Kopiert die Dateien requirements.txt und das aktuelle Verzeichnis in den Container
COPY requirements.txt ./

# Installiert die benötigten Python-Pakete
RUN pip install --no-cache-dir -r requirements.txt

# Kopiert den restlichen Code in den Container
COPY . .

# Setzt die Umgebungsvariable für Flask, um im Entwicklungsmodus zu laufen
ENV FLASK_ENV=development
ENV FLASK_APP=src/app.py

# Exponiert den Port 5000 (standardmäßiger Flask-Port) des Containers
EXPOSE 1337

# Kommando, das beim Start des Containers ausgeführt wird
CMD ["flask", "run", "--host=0.0.0.0", "--port=1337"]
