from flask import Flask, jsonify
import docker

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "Backend is running!"})

@app.route("/api/containers")
def list_containers():
    try:
        client = docker.from_env()
        containers = client.containers.list(all=True)
        result = []
        for c in containers:
            result.append({
                "id": c.short_id,
                "name": c.name,
                "status": c.status,
                "image": c.image.tags
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

