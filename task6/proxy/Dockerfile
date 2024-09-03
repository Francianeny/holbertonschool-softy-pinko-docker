# Utiliser l'image officielle Nginx comme base
FROM nginx:latest

# Copier la configuration de Nginx dans le conteneur
COPY ./proxy.conf /etc/nginx/conf.d/default.conf

# Exposer le port 80 pour Nginx
EXPOSE 80

# Commande par défaut pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
