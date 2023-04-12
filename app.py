from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key= 'asd'
@app.route('/hello')
def index():
    flash('whats ur name???????')
    return render_template('index.html')

@app.route('/greet',methods=['POST','GET'])
def greet():
    flash('hi '+str(request.form['name_input']))
    return render_template('index.html')
    
