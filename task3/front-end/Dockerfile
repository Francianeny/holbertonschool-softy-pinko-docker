# Utiliser l'image Nginx la plus récente
FROM nginx:latest

# Copier la configuration personnalisée de Nginx
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Copier les fichiers front-end dans le répertoire par défaut de Nginx
COPY ./softy-pinko-front-end /usr/share/nginx/html

# Exposer le port 80
EXPOSE 80
