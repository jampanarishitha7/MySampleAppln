<<<<<<< HEAD
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('myform.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    return render_template('greetings.html', name=username, mail=email)

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask
app = Flask(__name__)
@app.route('/')
def firstApp():
    return "Hello World Welcome"
if (__name__ == "__main__"):
    app.run(debug = True)  
>>>>>>> 7827d20eb15e8274d7b66eb07e65b547d6bf2101
