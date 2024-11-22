#!/bin/bash

mkdir -p /var/www/certbot/.well-known/acme-challenge/

certbot certonly --webroot -w /var/www/certbot -d coffeeinveins.ru -d www.coffeeinveins.ru --email book.anna.book@gmail.com --agree-tos --non-interactive

if [ -f /etc/letsencrypt/live/coffeeinveins.ru/fullchain.pem ]; then
    cp /etc/letsencrypt/live/coffeeinveins.ru/fullchain.pem /etc/nginx/cert.pem
else
    echo "Certificate not found! :(("
fi

if [ -f /etc/letsencrypt/live/coffeeinveins.ru/privkey.pem ]; then
    cp /etc/letsencrypt/live/coffeeinveins.ru/privkey.pem /etc/nginx/key.pem
else
    echo "Private key not found! :("
fi