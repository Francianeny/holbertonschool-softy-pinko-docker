# Utiliser l'image Ubuntu la plus récente comme base
FROM ubuntu:latest

# Mettre à jour la liste des paquets
RUN apt-get update

# Mettre à jour les logiciels installés
RUN apt-get upgrade -y

# Installer l'utilitaire 'curl' pour vérifier que le conteneur fonctionne
RUN apt-get install -y curl

# Démarrer une commande 'sleep' infinie pour garder le conteneur actif
CMD ["sleep", "infinity"]
