# Flask API

## Build 
docker build -t flask-api .

## Run 
docker run -ti -p 5050:5050 flask-api 

## Test
curl http://127.0.0.1:5050/health