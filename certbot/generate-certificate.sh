#!/bin/bash

rm -rf /etc/letsencrypt/live/coffeeinveins.ru

certbot certonly --webroot -w /var/www/certbot -d coffeeinveins.ru -d www.coffeeinveins.ru --email komy.kabachok@yandex.ru --agree-tos --non-interactive

rm -rf /etc/nginx/cert.pem
rm -rf /etc/nginx/key.pem

cp /etc/letsencrypt/live/coffeeinveins.ru/fullchain.pem /etc/nginx/cert.pem
cp /etc/letsencrypt/live/coffeeinveins.ru/privkey.pem /etc/nginx/key.pem
