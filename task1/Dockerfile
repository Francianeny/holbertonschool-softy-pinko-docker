# Utilisez l'image de base Ubuntu
FROM ubuntu:latest

# Met à jour les paquets APT et installe Python et pip
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip

# Installe Flask via pip
RUN pip3 install flask

# Définit le répertoire de travail
WORKDIR /app

# Copie le fichier de l'application Flask dans le conteneur
COPY api.py /app/api.py

# Exécute l'application Flask
CMD ["python3", "/app/api.py"]
