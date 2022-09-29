from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def home():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')

if __name__=='main_':
    app.run(host='0.0.0.0',port=8080,debug=True)