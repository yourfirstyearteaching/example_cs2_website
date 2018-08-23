from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/schedule/')
def schedule():
    return render_template('schedule.html')

@app.route('/assignents/')
@app.route('/assignments/<path:assign>')
def assignments(assign=None):
    print(request.script_root)
    if not assign:
        return render_template("assignments/assignments.html")
    return render_template("assignments/"+assign)

if __name__ == '__main__':
    app.run()

