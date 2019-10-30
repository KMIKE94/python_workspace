# Internally the Flask app is still created but it now has
# Added functionality using connextion

# from flask import(
#     Flask,
#     render_template
# )
from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

# create the application instance
# app = Flask(__name__, template_folder="templates")

# create the url route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)