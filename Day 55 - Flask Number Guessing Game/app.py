from flask import Flask, render_template

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/products')
def products ():
    return 'This is a product page.'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you're {number} years old."

if __name__ == "__main__":
    app.run(debug= True)