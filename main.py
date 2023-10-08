from flask import Flask 
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)         # Инициализация
@app.route("/")               # Указание маршрута
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) 