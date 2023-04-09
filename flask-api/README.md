# Flask API

## Build 
docker build -t flask-api .

## Run 
docker run -ti -p 5050:5050 -e FLASK_ENVIRONMENT=production flask-api 

## Test
curl http://127.0.0.1:5050/health
curl -X POST -H "Content-Type: application/json" -d '{"name": "job-1"}' http://localhost:5050/jobs


### Environment variables
`FLASK_ENVIRONMENT`

>By default a `FLASK_ENVIRONMENT` defined in Dockerfile with a `dev` value and can be overwriten with `-e` key of `docker run` command by the `production` value

`FLASK_REDIS_HOST`
`FLASK_REDIS_PORT`
