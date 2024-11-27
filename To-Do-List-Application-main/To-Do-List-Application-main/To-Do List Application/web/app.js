const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

// Load tasks from the server
function loadTasks() {
  fetch("http://127.0.0.1:5000/tasks")
    .then((response) => response.json())
    .then((tasks) => renderTasks(tasks))
    .catch((err) => console.error("Error loading tasks:", err));
}

// Add a task
function addTask() {
  const taskText = taskInput.value.trim();
  if (taskText) {
    fetch("http://127.0.0.1:5000/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task: taskText }),
    })
      .then((response) => response.json())
      .then(() => {
        taskInput.value = "";
        loadTasks(); // Reload tasks
      })
      .catch((err) => console.error("Error adding task:", err));
  }
}

// Delete a task
function deleteTask(index) {
  fetch(`http://127.0.0.1:5000/tasks/${index}`, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then(() => loadTasks()) // Reload tasks
    .catch((err) => console.error("Error deleting task:", err));
}

// Render tasks to the UI
function renderTasks(tasks) {
  taskList.innerHTML = "";
  tasks.forEach((task, index) => {
    const listItem = document.createElement("li");
    listItem.innerHTML = `${task} <button onclick="deleteTask(${index})">Delete</button>`;
    taskList.appendChild(listItem);
  });
}

// Load tasks when the page loads
document.addEventListener("DOMContentLoaded", loadTasks);
