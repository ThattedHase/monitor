from flask import Flask, render_template, request, redirect, url_for
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename





app = Flask(__name__)

UPLOAD_FOLDER = '/instance/time_table'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

users = {'Ярослав': '1234','саня':'1234'}



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

@app.route('/upload')
def main1():
    return render_template('upload.html')

@app.route('/uploadtest1')
def uploadtest1():
    return render_template('upl.html')

@app.route('/uploadtest', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Файл не выбран'
    
    file = request.files['file']

    if file.filename == '':
        return 'Файл не выбран'

    # Можно сохранить файл в нужную директорию или обработать его по-другому
    # Пример сохранения в папку 'uploads' в текущей директории
    file.save('D:\monitor\instance\time_table' + file.filename)

    return 'Файл успешно загружен'

if __name__ == '__main__':
    app.run(debug=True)
