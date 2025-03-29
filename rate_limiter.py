from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(decode_responses=True)


RATE_LIMIT = 5        # Max requests allowed
WINDOW_SECONDS = 60   # Time window in seconds


def is_rate_limited(ip):
    key = f"rate:{ip}"
    current = r.incr(key)
    if current == 1:
        # First request — set expiry on key
        r.expire(key, WINDOW_SECONDS)

    return current > RATE_LIMIT

@app.route("/")
def home():
    ip = request.remote_addr()
    if is_rate_limited(ip):
        ttl = r.ttl(f"rate:{ip}")
        return jsonify({
            "error": "Rate limit exceeded",
            "retry_after": ttl
        }), 429

    return jsonify({
        "message": "Request successful",
        "remaining": RATE_LIMIT - r.get(f"rate:{ip}")
    })
