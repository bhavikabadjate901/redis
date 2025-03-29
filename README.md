# 🚀 Redis Key-Value Storage – Basics & Usage

This repository provides a beginner-friendly yet practical overview of **Key-Value (KV) storage**, with a strong focus on **Redis** — a powerful in-memory data store used widely in the industry for caching, real-time analytics, queues, and more.

---

## 🔑 What Is KV Storage?

A **Key-Value store** is a simple database that stores data as a dictionary-like structure:

key => value

Redis is one of the fastest and most flexible key-value databases available.

---

## 📚 What You'll Learn

- 💡 Basics of KV storage and Redis architecture
- ⚙️ Redis data types: Strings, Hashes, Lists, Sets, and Sorted Sets
- 🧪 Redis CLI usage
- 🧠 Real-world projects using Redis:
  - ✅ To-Do List App
  - ⏳ Rate Limiter
  - 📋 Job Queue System

---

## 🛠️ Prerequisites

- Python 3.7+
- Redis (installed locally or via Docker)
- Flask (for app demos)

### 🔧 Install dependencies:

```bash
pip install flask redis
```

### 🧱 Run Redis:
```bash
# macOS (Homebrew)
brew install redis
brew services start redis
```

```bash
# OR using Docker
docker run --name redis -p 6379:6379 -d redis
```

### 📂 Project Structure

```bash
.
├── cli/                # Redis CLI examples
│   └── todo-redis-cli.txt
├── flask-apps/         # Flask apps using Redis
│   ├── todo_app.py     # To-Do List API
│   ├── rate_limiter.py # IP-based Rate Limiting
│   └── task_queue.py   # Simulated job queue
└── README.md
```

### 🧪 Redis CLI Examples

```bash
# Set a key
SET name "Alice"

# Get a key
GET name

# Hash (like a user object)
HSET user:1 name "Bob" age 30
HGETALL user:1

# List (queue)
LPUSH tasks "task1"
RPOP tasks

# Sorted Set (leaderboard)
ZADD scores 500 "player1"
ZREVRANGE scores 0 -1 WITHSCORES
```

### ✅ To-Do App with Flask + Redis
Use Redis List to manage tasks.

```bash
cd flask-apps
python todo_app.py
```

Then open in browser:

Add task: ```http://localhost:5000/add?task=Read%20book```

View tasks: ```http://localhost:5000/tasks```

Mark done: ```http://localhost:5000/done```

Clear all: ```http://localhost:5000/clear```

### ⏳ Rate Limiter (IP-Based)
Tracks requests per IP and limits users to 5 requests per minute.

```bash
cd flask-apps
python rate_limiter.py
```

Visit http://localhost:5000/ multiple times. After 5 requests within a minute, you'll get:

```json
{
  "error": "Rate limit exceeded",
  "retry_after": 42
}
```

### 📋 Job Queue with Redis
Simulate background workers using LPUSH and BRPOP.

Producer:
```bash
python producer.py
Worker:
```

```bash
python worker.py
```

The worker will wait and process tasks in real-time.

### 💡 Advanced Ideas to Explore
Redis Streams (for logs or pipelines)

Redis Geo (for nearby search)

Redis Pub/Sub (for real-time messaging)

Use Redis as a cache in Flask/Django apps

Store session tokens with TTL

### 📘 References
Redis.io Documentation

Redis Cheat Sheet

Awesome Redis GitHub

### 🧠 Contributing
PRs welcome! Feel free to add examples, improvements, or fixes.

### 📜 License
MIT License

```yaml
---

Just copy, paste, commit it as `README.md`, and your GitHub repo will look ✨ awesome. Want me to help generate a `requirements.txt` too?
```
