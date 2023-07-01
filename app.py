from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')

def login():
    return render_template('login.html')

@app.route('/home')

def home():
    return render_template('home.html')


@app.route('/contact')

def contact():
    return render_template('contact.html')


@app.route('/Registration')

def contact():
    return render_template('contact.html')



if __name__=="__main__":
    app.run(debug=True)