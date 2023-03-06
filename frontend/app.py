from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/output')
def output():
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True)
