from flask import Flask, render_template 

# Create a Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    post = [
        {"id": 1, "title": "Postingan Pertama", "Konten": "Ini Adalah Postingan Pertama Saya."},
        {"id": 2, "title": "Postingan Kedua", "Konten": "Ini Adalah Postingan Kedua Saya."}
    ]
    return render_template('index.html', title="Welcome To My Website", post=post)

# About Route
@app.route('/about')
def about():
    return render_template('About.html')

# Selamat Route
@app.route('/selamat/<nama>')
def selamat(nama):
    return render_template('selamat.html', nama=nama)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Error.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)