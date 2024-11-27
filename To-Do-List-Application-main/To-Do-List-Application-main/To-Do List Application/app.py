from flask import Flask, jsonify, request
import json

app = Flask(__name__)
TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Retrieve all tasks."""
    tasks = load_tasks()
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    """Add a new task."""
    tasks = load_tasks()
    new_task = request.json.get("task")
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        return jsonify({"message": "Task added successfully"}), 201
    return jsonify({"error": "Task content is missing"}), 400


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"error": "Invalid task ID"}), 400


if __name__ == "__main__":
    app.run(debug=True)
