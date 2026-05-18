from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Todo List</title>
    <style>
        body{
            font-family: Arial;
            background:#f4f4f4;
            text-align:center;
            margin-top:50px;
        }
        .container{
            width:400px;
            margin:auto;
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0 0 10px gray;
        }
        input{
            width:70%;
            padding:10px;
        }
        button{
            padding:10px;
            cursor:pointer;
        }
        ul{
            padding:0;
        }
        li{
            list-style:none;
            background:#eee;
            margin:10px 0;
            padding:10px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }
        .done{
            text-decoration:line-through;
            color:gray;
        }
        a{
            text-decoration:none;
            margin-left:10px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Todo List</h1>

    <form action="/add" method="post">
        <input type="text" name="task" placeholder="Enter task" required>
        <button type="submit">Add</button>
    </form>

    <ul>
        {% for task in tasks %}
        <li>
            <span class="{% if task.done %}done{% endif %}">
                {{ task.name }}
            </span>

            <div>
                <a href="/complete/{{ loop.index0 }}">✔️</a>
                <a href="/delete/{{ loop.index0 }}">❌</a>
            </div>
        </li>
        {% endfor %}
    </ul>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append({'name': task, 'done': False})
    return redirect('/')

@app.route('/complete/<int:index>')
def complete(index):
    tasks[index]['done'] = not tasks[index]['done']
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)