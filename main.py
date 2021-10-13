# Python Library Imports

#Flask App
from flask import Flask, request, render_template, redirect

# Creating Flask App object
app = Flask(__name__, template_folder="templates")

expenses = []

# Each method in the Flask app is tied to a url, which is wriiten using '@app.route()'
@app.route('/')
def root():
    # Default an HTML page
    return render_template('index.html')

# Render add expense page
@app.route('/add-page')
def add_page():
    pass

# Render view page with specific category filter
@app.route('/view-cat', methods=['POST'])
def change_category():
    pass
    
# Regular GET method (doesn't receive information, sends back information)
@app.route('/view/<category>')
def view(category):
    pass

# POST method (receives information, sends back information)
@app.route('/add', methods=['POST'])
def add_item():
    pass

# Runs Flask App
if __name__ == "__main__":
    app.run()