--------------------
      ON SERVER
--------------------


docker-compose up --build -d

docker exec -it nginx /bin/sh

certbot --nginx -d coffeeinveins.ru -d www.coffeeinveins.ru


docker-compose exec nginx nginx -t
docker-compose exec nginx nginx -s reload
   

-----------------------------
Just useful Docker commands
-----------------------------

docker-compose build

    # docker-compose down
    # docker-compose down --remove-orphans
    # docker-compose build --no-cache
    # docker-compose down -v

docker-compose up