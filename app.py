from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name)

# Function to load tasks from the "demo2.txt" file
def load_tasks():
    try:
        with open("demo2.txt", "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to the "demo2.txt" file
def save_tasks(tasks):
    with open("demo2.txt", "w") as file:
        file.write("\n".join(tasks))

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/mark_done/<int:task_id>')
def mark_done(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id] = "[Done] " + tasks[task_id]
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/remove_task/<int:task_id>')
def remove_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)