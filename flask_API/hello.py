from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text=function()
        return f"<b>+{text}+</b>"
    return wrapper_function

@app.route("/")
def hello_world():
    return "<H2>Hello, World!</H2>"

@app.route("/bye")
@make_bold
def bye():
    return " bye"

@app.route("/user/<name>")
def value(name):
    return f"hello {name}"

if __name__=='__main__':
    app.run(debug=True)