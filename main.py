from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a greeting message."""
    return "Hello, World!"


@app.route('/<name>')
def hello_name(name):
    """Return a personalized greeting."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
