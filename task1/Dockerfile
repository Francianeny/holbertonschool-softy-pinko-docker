# Utiliser la dernière version de l'image Ubuntu
FROM ubuntu:latest

# Mettre à jour les dépôts de paquets et installer les paquets nécessaires
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip

# Installer Flask avec pip3
RUN pip3 install flask

# Ajouter une ligne pour éviter les erreurs de gestion de l'environnement
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier api.py dans l'image Docker
COPY api.py /app/api.py

# Exposer le port 5252
EXPOSE 5252

# Définir la commande pour exécuter l'application Flask
CMD ["python3", "/app/api.py"]
