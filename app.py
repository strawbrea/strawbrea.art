from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdf/<filename>')
def serve_pdf(filename):
    return send_from_directory('static/pdf', filename)

@app.route('/left_panel')
def left_panel():
    return render_template('left_panel.html')

@app.route('/right_panel')
def right_panel():
    return render_template('right_panel.html')

@app.route('/projects')
def projects():
    return "<h1>Projects Page Coming Soon!</h1>"

if __name__ == '__main__':
    app.run(debug=True)