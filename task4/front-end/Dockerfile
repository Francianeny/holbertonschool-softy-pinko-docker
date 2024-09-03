# Utilise l'image de base Nginx
FROM nginx:latest

# Copie les fichiers du front-end dans le répertoire par défaut de Nginx
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf
