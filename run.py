import os # you import this to utilise environment variables, e.g DB connection strings, API keys & sensitive info you don't want to hard code into your files
from taskmanager import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
