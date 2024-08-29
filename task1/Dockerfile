# Utiliser la dernière version d'Ubuntu
FROM ubuntu:latest

# Mettre à jour et mettre à niveau le système
RUN apt-get update && apt-get upgrade -y

# Installer Python3 et pip3
RUN apt-get install -y python3 python3-pip python3-venv

# Créer un environnement virtuel pour Python
RUN python3 -m venv /venv

# Activer l'environnement virtuel et installer Flask
RUN /venv/bin/pip install flask

# Copier le script Python dans le conteneur
COPY api.py /app/api.py

# Définir le répertoire de travail
WORKDIR /app

# Exposer le port sur lequel Flask écoute
EXPOSE 5252

# Exécuter l'application Flask
CMD ["/venv/bin/python", "/app/api.py"]
