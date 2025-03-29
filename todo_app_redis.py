from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(decode_responses=True)

LIST_NAME = "todo:list"

@app.route("/")
def home():
    return jsonify({"message": "Redis To-Do API is running!"})

# Add a task
@app.route("/add", methods=["POST"])
@app.route("/add", methods=["GET"])
def add_task():
    task = request.args.get("task")
    if not task:
        return jsonify({"error": "Missing ?task= parameter"}), 400

    r.lpush(LIST_NAME, task)
    return jsonify({"message": "Task added", "task": task})

# View all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = r.lrange(LIST_NAME, 0, -1)
    return jsonify({"tasks": tasks})

# Mark last task as done (pop)
@app.route("/done", methods=["GET"])
def mark_done():
    task = r.rpop(LIST_NAME)
    if task:
        return jsonify({"message": "Task completed", "task": task})
    else:
        return jsonify({"message": "No tasks left!"})

# Clear all tasks
@app.route("/clear", methods=["GET"])
def clear_tasks():
    r.delete(LIST_NAME)
    return jsonify({"message": "Cleared all tasks!"})

if __name__ == "__main__":
    app.run(debug=True)