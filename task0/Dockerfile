# Utiliser l'image Ubuntu la plus récente
FROM ubuntu:latest

# Mettre à jour et mettre à niveau les packages
RUN apt-get update && apt-get upgrade -y

# Installer Python3 et pip3
RUN apt-get install -y python3 python3-pip

# Installer Flask
RUN pip3 install flask

# Supprimer le fichier EXTERNALLY-MANAGED pour éviter les erreurs lors de l'installation de packages
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier Python dans le conteneur
COPY api.py /app/api.py

# Définir la commande d'exécution
CMD ["python3", "api.py"]
