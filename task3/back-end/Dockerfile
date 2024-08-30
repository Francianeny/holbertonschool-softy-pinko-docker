# Utiliser l'image de base Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système (nécessaires pour l'installation de certains packages Python)
RUN apt-get update && apt-get install -y \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Créer un environnement virtuel pour Python
RUN python3 -m venv /venv

# Activer l'environnement virtuel et mettre à jour pip
RUN /venv/bin/pip install --upgrade pip

# Copier les fichiers de dépendances dans le conteneur
COPY requirements.txt ./

# Installer les dépendances de l'application dans l'environnement virtuel
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application Flask sera disponible
EXPOSE 5252

# Définir la variable d'environnement pour Flask
ENV FLASK_APP=api.py

# Commande pour démarrer l'application Flask
CMD ["/venv/bin/flask", "run", "--host=0.0.0.0", "--port=5252"]
