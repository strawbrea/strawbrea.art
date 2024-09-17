from flask import Flask, render_template

app = Flask(__name__)

# Main index route that serves the page with iframes
@app.route('/')
def index():
    return render_template('index.html')

# Left panel content
@app.route('/left-panel')
def left_panel():
    return render_template('left-panel.html')

# Right panel content
@app.route('/right-panel')
def right_panel():
    return render_template('right-panel.html')

if __name__ == '__main__':
    app.run(debug=True)