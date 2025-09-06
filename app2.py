# Templates and HTML

from flask import Flask, render_template, redirect, url_for

app= Flask(__name__, template_folder='templates')

@app.route('/hello')
def hello():
    list= [1, 2, 3, 4]
    return render_template('index.html', list=list)

@app.route('/other')
def other():
    text= 'this is text'
    return render_template('other.html', text= text)

@app.route('/redirect')
def redirect_endpoint():
    return redirect(url_for('other'))

# custom template filters

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1] # to reverse string

@app.template_filter('repeat')
def repeat(s, time= 2):
    return s * time # to reverse string

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)