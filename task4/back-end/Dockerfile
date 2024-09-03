# Utilise l'image de base Ubuntu
FROM ubuntu:latest

# Met à jour les paquets et installe Python et pip
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip

# Installe les dépendances Python
RUN pip3 install flask flask-cors

# Définit le répertoire de travail
WORKDIR /app

# Copie le code source de l'API dans le conteneur
COPY ./api.py /app/api.py

# Expose le port 5252 pour accéder au back-end
EXPOSE 5252

# Commande pour exécuter l'application Flask
CMD ["python3", "api.py"]
