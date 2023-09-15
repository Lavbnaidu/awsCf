from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def welcome():
    return render_template('home.html')

# Run the app
if __name__ == '__main__':
    app.run()