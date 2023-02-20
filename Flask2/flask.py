from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    number = request.args.get('number')
    if not number:
        return 'Error: no query parameter included'
    try:
        number = int(number)
        if number % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
    except ValueError:
        result = 'not an integer'
    return render_template('result.html', number=number, result=result)

if __name__ == '__main__':
    app.run()
