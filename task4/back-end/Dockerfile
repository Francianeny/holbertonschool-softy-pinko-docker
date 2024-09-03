# Utiliser l'image de base Python
FROM python:3.8-slim

# Installer Flask et Flask-Cors
RUN pip install flask flask-cors

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier api.py dans le conteneur
COPY api.py /app/api.py

# Exposer le port 5252
EXPOSE 5252

# Lancer l'application Flask
CMD ["python", "api.py"]
