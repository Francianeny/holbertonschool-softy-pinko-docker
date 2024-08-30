# Utiliser l'image Nginx la plus récente
FROM nginx:latest

# Copier les fichiers front-end dans le répertoire du serveur web Nginx
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copier la configuration de Nginx
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf
