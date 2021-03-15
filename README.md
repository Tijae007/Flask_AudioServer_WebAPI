# Audio details


# How to run
1. Set up the DB details in .env
2. Set up the PostgreSQL with
   > docker-compose --project-name binary up --remove-orphan --build -d
3. DB details are found in [init.sql](queries/init.sql)
4. `docker-compose config` shows the docker configurations that exist
5. Create a virtualenv, activate it and install the libraries in [requirements.txt](requirements.txt)
6. Ensure that you run migrations. See the #migrations section below
7. Run the project with `FLASK_APP=wsgi.py FLASK_ENV=development flask run`
8. Run the shell with `FLASK_APP=wsgi.py FLASK_ENV=development flask shell`

# migrations
1. Initiate the DB with `FLASK_APP=wsgi.py flask dbi`
2. Run migration with `FLASK_APP=wsgi.py flask dbm`
3. Run upgrade with `FLASK_APP=wsgi.py flask dbu-no-sql`

# run tests
 python -m unittest discover

# SONG requests
1. curl -X POST http://127.0.0.1:5000/apiv1/create \
    -H "Content-Type: application/json" \
      -d '{"audioFileType": "Song", "audioFileMetadata":{"name": "March for Love", "duration": 204}}'

2. curl -X GET http://127.0.0.1:5000/apiv1/get/Song/1 -H "Content-Type: application/json"

3. curl -X PUT http://127.0.0.1:5000/apiv1/update/Song/1 \
   -H "Content-Type: application/json" \
      -d '{"audioFileMetadata":{"name": "Pink - Family Portrait", "duration": 359}}'

4. curl -X DELETE http://127.0.0.1:5000/apiv1/delete/Song/1 -H "Content-Type: application/json" -d '{}'   

# PODCAST requests
1. curl -X POST http://127.0.0.1:5000/apiv1/create \
    -H "Content-Type: application/json" \
      -d '{"audioFileType": "Podcast", "audioFileMetadata":{"name": "Twice as Tall", "duration": 354, "host": "Rick Dees", "participants": ["Burna boy"]}}'

2. curl -X GET http://127.0.0.1:5000/apiv1/get/Podcast/1 -H "Content-Type: application/json"

3. curl -X PUT http://127.0.0.1:5000/apiv1/update/Podcast/1 \
   -H "Content-Type: application/json" \
      -d '{"audioFileMetadata":{"name": "Twice as Talls", "duration": 354, "host": "Rick Dee", "participants": ["Burna boy", "DJ Jimmy"]}}'

4. curl -X DELETE http://127.0.0.1:5000/apiv1/delete/Podcast/1 -H "Content-Type: application/json" -d '{}'

# AUDIOBOOK requests
1. curl -X POST http://127.0.0.1:5000/apiv1/create \
    -H "Content-Type: application/json" \
      -d '{"audioFileType": "Audiobook", "audioFileMetadata":{"title": "Twice as Tall", "author": "Yunus", "narrator": "Yunus2", "duration": 100}}'

2. curl -X GET http://127.0.0.1:5000/apiv1/get/Audiobook/1 -H "Content-Type: application/json"

3. curl -X PUT http://127.0.0.1:5000/apiv1/update/Audiobook/1 \
   -H "Content-Type: application/json" \
      -d '{"audioFileMetadata":{"title": "Twice as Tall-2", "author": "Yunus", "narrator": "Yunus2", "duration": 100}}'

4. curl -X DELETE http://127.0.0.1:5000/apiv1/delete/Audiobook/1 -H "Content-Type: application/json" -d '{}'
