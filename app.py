from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!doctype html>
        <html lang="en">
          <head>
            <title>Priority To-Do</title>
          </head>
          <body>
            <h1>Priority To-Do List</h1>
            <form>
              <input type="text" id="new_task" placeholder="Enter a task">
              <select id="priority">
                <option>High</option>
                <option>Medium</option>
                <option>Low</option>
              </select>
              <button type="submit">Add Task</button>
            </form>
            <ul id="task_list">
            </ul>
          </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
