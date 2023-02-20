from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%B %d, %Y")
    return render_template('index.html', current_time=current_time, current_date=current_date)

if __name__ == "__main__":
    app.run()
