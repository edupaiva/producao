from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def iniciar():
    return render_template('lista.html')


app.run()