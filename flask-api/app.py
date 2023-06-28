from flask import Flask, jsonify, request
import os
import redis

app = Flask(__name__)

redis_connection = redis.Redis(host=os.environ.get('FLASK_REDIS_HOST', 'redis'), port=os.environ.get('FLASK_REDIS_PORT', '6379'))

@app.route('/health')
def health_check():
    return 'OK', 200

@app.route('/environment')
def environment():
    environment = os.environ.get('FLASK_ENVIRONMENT', 'unknown')
    return jsonify({'environment': environment})

@app.route('/jobs', methods=['POST'])
def add_job():
    data = request.get_json()
    name = data.get('name')
    redis_connection.lpush('jobs', name) # add the job to the Redis queue
    return '', 204

@app.route('/all-jobs')
def all_jobs():
    jobs = [job.decode() for job in redis_connection.lrange('jobs', 0, -1)] # get all jobs from Redis queue
    return jsonify({'jobs': jobs})

if __name__ == '__main__':
    app.run(port=5050)