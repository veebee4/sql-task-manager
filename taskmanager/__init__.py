import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"): # in order to use hidden variables in env.py (hidden by gitignore), need to import 'env' package which will only import if it sees "env.py"
    import env
    

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes # imported last as it relies on app and db var's defined above