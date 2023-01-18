from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kingkong'
@app.route('/')
@app.route('/home')
def home():
    flash("What's your name?")
    return render_template("home.html")


@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash("Hi " + str(  request.form['name_input']) + ", great to see you!!")
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
    
