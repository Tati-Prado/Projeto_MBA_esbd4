from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)
app.secret_key = 's3cr3t'

# Banco de dados em memória para simulação
task_list = []

@app.route('/', methods=['GET', 'POST'])
def home():
    global task_list
    if request.method == 'POST':
        # Recebe a tarefa e a prioridade do formulário
        task = request.form['task']
        priority = request.form['priority']
        task_list.append({'task': task, 'priority': priority, 'id': len(task_list) + 1})
        return redirect(url_for('home'))

    # Renderiza a página com a lista de tarefas
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <title>Priority To-Do</title>
          </head>
          <body>
            <h1>Priority To-Do List</h1>
            <form method="post">
              <input type="text" name="task" id="new_task" placeholder="Enter a task" required>
              <select name="priority" id="priority">
                <option>High</option>
                <option>Medium</option>
                <option>Low</option>
              </select>
              <button type="submit">Add Task</button>
            </form>
            <ul id="task_list">
              {% for item in task_list %}
                <li>{{ item.id }} - {{ item.task }} - prioridade {{ item.priority }}</li>
              {% endfor %}
            </ul>
          </body>
        </html>
    ''', task_list=task_list)

if __name__ == '__main__':
    app.run(debug=True)
