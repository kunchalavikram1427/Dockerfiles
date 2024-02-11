from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import time
import datetime
import socket

INTIAL_DELAY = int(os.getenv('INTIAL_DELAY', '5'))
print(f'Waiting for the app to start')
time.sleep(INTIAL_DELAY)

app = Flask(__name__)

# Change Database URI
database_uri = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite')

# App initialization
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Get Hostname
hostname = socket.gethostname()

# DB Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Create initial table
with app.app_context():
    db.create_all()

# Health/details Route
@app.route("/details")
@app.route("/health")
def health():
    ts = time.time()
    return jsonify(
        status="running",
        timestamp=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
        hostname=hostname
    )

# Homepage Route
@app.get("/")
def home():
    todo_list = db.session.query(Todo).all()
    db.session.remove()
    db.engine.dispose()
    return render_template("base.html", todo_list=todo_list, hostname=hostname)

# Add Route 
@app.post("/add")
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    db.session.remove()
    db.engine.dispose()
    return redirect(url_for("home"))

# Update Route
@app.get("/update/<int:todo_id>")
def update(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    db.session.remove()
    db.engine.dispose()
    return redirect(url_for("home"))

# Delete Route
@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    db.session.remove()
    db.engine.dispose()
    return redirect(url_for("home"))

# Start the flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
	