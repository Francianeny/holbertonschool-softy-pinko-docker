# Utiliser l'image Nginx la plus récente
FROM nginx:latest

# Copier les fichiers front-end dans le répertoire du serveur web Nginx
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copier la configuration de Nginx
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Copier le fichier de configuration Nginx
COPY default.conf /etc/nginx/conf.d/default.conf

# Copier les fichiers de build dans le répertoire par défaut de Nginx
COPY ./build /usr/share/nginx/html

# Copier la configuration personnalisée de Nginx
COPY ./nginx.conf /etc/nginx/nginx.conf

# Exposer le port 80
EXPOSE 80
