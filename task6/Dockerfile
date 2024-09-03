# Utiliser l'image officielle de Python comme base
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY api.py /app/api.py

# Installer Flask et autres dépendances nécessaires
RUN pip install flask flask-cors

# Exposer le port utilisé par Flask
EXPOSE 5000

# Démarrer l'application
CMD ["python", "api.py"]
