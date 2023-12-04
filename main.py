from flask import Flask, render_template, request, redirect, url_for
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory




app = Flask(__name__)

UPLOAD_FOLDER = '/instance/time_table'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

users = {'иван': '1234','саня':'1234'}



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Проверка наличия пользователя в "базе данных"
        if username in users and users[username] == password:
            # Перенаправление на главную страницу после успешной аутентификации
            return redirect(url_for('main'))
        else:
            return render_template('login.html')

    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')  # Provide feedback to the user
        return redirect(url_for('main'))
    else:
        flash('Invalid file format')  # Provide feedback to the user
        return redirect(request.url)

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == '__main__':
    app.run(debug=True)
