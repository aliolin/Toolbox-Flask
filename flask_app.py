from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return render_template('profile.html', firstname = request.form['name'], age = request.form['age'], favninja = 'Patrick Huston')

if __name__ == '__main__':
    app.run()
