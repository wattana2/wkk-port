from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def profile():
    return render_template('profile.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
