from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Creating a Flask App
app = Flask(__name__)


# Connecting the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://whvjomzrmlxmbh:096b146b6cd1fea76ec36806e8e96297183d1a613c8ad84e6d8c9c51390470e2@ec2-3-229-11-55.compute-1.amazonaws.com:5432/dbpmdgbljs1754'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Creating a Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())


# Default Hello World
@app.route("/")
def home():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
