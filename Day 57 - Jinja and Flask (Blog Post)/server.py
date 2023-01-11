from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    random_number =  random.randint(0, 10)
    current_year = datetime.now().year
    return render_template('index.html', num = random_number, year = current_year )

@app.route('/guess/<name>')
def guess(name):
    age = requests.get(f"https://api.agify.io/?name={name}").json()['age']
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()['gender']
    return render_template("guess.html", name = name, age = age, gender = gender)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/48510a577ff518ac8b4f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts)

if __name__ == "__main__":
    app.run(debug= True)