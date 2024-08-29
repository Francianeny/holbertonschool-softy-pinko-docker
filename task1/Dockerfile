# Utiliser la dernière version de l'image Ubuntu
FROM ubuntu:latest

# Mettre à jour les dépôts de paquets
RUN apt-get update

# Mettre à niveau les paquets existants
RUN apt-get upgrade -y

# Installer Python3 et pip3
RUN apt-get install -y python3 python3-pip

# Installer Flask via pip3
RUN pip3 install flask

# Supprimer le fichier EXTERNALLY-MANAGED pour éviter les erreurs avec pip
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier Python dans le conteneur
COPY api.py /app/api.py

# Exposer le port 5252 pour accéder à l'application Flask
EXPOSE 5252

# Commande à exécuter lorsque le conteneur démarre
CMD ["python3", "api.py"]
