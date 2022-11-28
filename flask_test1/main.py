from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    janelas = 7
    return f"<p>Hello, {janelas} World!</p>"
if __name__ == '__main__':
    app.run(debug=True)

