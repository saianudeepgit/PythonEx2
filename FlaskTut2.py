from flask import Flask, redirect , url_for

app = Flask(__name__)


@app.route("<sai>")
def user(name):
   return f"hello {name}!"

if __name__ == "__main__":
    app.run()