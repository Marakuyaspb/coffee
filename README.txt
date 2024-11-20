--------------------
      ON SERVER
--------------------


docker-compose up --build -d

docker exec -it nginx /bin/sh

certbot --nginx -d coffeeinveins.ru -d www.coffeeinveins.ru



-----------------------------
Just useful Docker commands
-----------------------------

docker-compose build

    # docker-compose down
    # docker-compose down --remove-orphans
    # docker-compose build --no-cache
    # docker-compose up --verbose
    # docker-compose down -v

docker-compose up


openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes \
-keyout ssl/co.key -out ssl/co.crt \
-subj '/CN=*.coffeeinveins.ru' \
-addext 'subjectAltName=DNS:*.coffeeinveins.ru'


openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes 
-keyout ssl/co.key -out ssl/co.crt 
-subj '/CN=coffeeinveins.ru' 
-addext 'subjectAltName=DNS:coffeeinveins.ru,DNS:*.coffeeinveins.ru'
