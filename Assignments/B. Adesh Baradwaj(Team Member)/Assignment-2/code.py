from flask import Flask, render_template

app=Flask(_name_)

@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/about')
def home():
    return render_template('About.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/signin')
def signin():
    return render_template('Login.html')

if _name=='main_':
    app.run(host='0.0.0.0',port=8080,debug=True)