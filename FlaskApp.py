from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/user/')
def user():
    return render_template('hello.html', user=True)

@app.route('/user/<name>')
def user_name(name):
    if name == "artem" or name == "Artem":
        abort(404)
    else:
        return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
