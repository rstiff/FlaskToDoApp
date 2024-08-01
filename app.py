#Name:

#Project Name: Flask App


from flask import Flask, render_template, request, redirect, url_for
import MySQLdb


app = Flask(__name__)

class Todo:
    def __init__(self):
        # Database connection
        self.db = MySQLdb.connect(
            host='pass',
            user='pass',
            password='pass',
            database='pass'
        )
        self.cursor = self.db.cursor()

    @app.route('/')
    def load_todo():
        # Execute SQL query
        todo.cursor.execute("SELECT * FROM todos")
        todos = todo.cursor.fetchall()
        return render_template("index.html", todos=todos)
    
    @app.route("/add", methods=['POST'])
    def add():
        task = request.form['task']
        todo.cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
        todo.db.commit()
        return redirect(url_for('load_todo'))
    
    @app.route('/delete/<int:todo_id>')
    def delete(todo_id):
        todo.cursor.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
        todo.db.commit()
        return redirect(url_for("load_todo"))
    

# Create an instance of the Todo class
todo = Todo()

if __name__ == "__main__":
    app.run(debug=True)
    #http://127.0.0.1:5000
