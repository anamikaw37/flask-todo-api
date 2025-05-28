from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
#in memory store for tasks
tasks = {}
@app.route("/")
def home():
    return "Hello, Azure! Flask is running."


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data.get('title', ''),
        "description": data.get('description', ''),
        "status": "pending"
    }
    tasks[task_id] = task
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods = ['DELETE'])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return '', 204
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run()
        
    
    