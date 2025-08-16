from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Configure Redis connection
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0, decode_responses=True)

@app.route("/")
def index():
    # Increment the visit counter
    visits = redis_client.incr("visit_count")
    return jsonify(message="Welcome to the Flask app!", visit_count=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
