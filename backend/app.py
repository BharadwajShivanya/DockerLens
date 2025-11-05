from flask import Flask, jsonify
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/containers')
def list_containers():
    containers = []
    for container in client.containers.list(all=True):
        containers.append({
            'id': container.short_id,
            'name': container.name,
            'status': container.status,
            'image': container.image.tags
        })
    return jsonify(containers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

