#!/bin/bash

rm -rf /etc/letsencrypt/live/coffeeinveins.ru

if certbot certonly --standalone --preferred-challenges http -d coffeeinveins.ru -d www.coffeeinveins.ru --email marakuyaspb@gmail.com --agree-tos --non-interactive; then
	echo "Certificate obtained successfully."
	rm -rf /etc/nginx/cert.pem
	rm -rf /etc/nginx/key.pem

	cp /etc/letsencrypt/live/coffeeinveins.ru/fullchain.pem /etc/nginx/cert.pem
	cp /etc/letsencrypt/live/coffeeinveins.ru/privkey.pem /etc/nginx/key.pem
else
    echo "Failed to obtain certificate!! (((((("
    exit 1
fi