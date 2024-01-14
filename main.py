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
    if 'file1' not in request.files and 'file2' not in request.files:
        return render_template('result.html', filename1="файл не выбран", filename2="файл не выбран")

    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 and not file2:
        return render_template('result.html', filename1="файл не выбран", filename2="файл не выбран")
    elif not file1:
        return render_template('result.html', filename1="файл не выбран", filename2=file2.filename)
    elif not file2:
        return render_template('result.html', filename1=file1.filename, filename2="файл не выбран")

    # Можно сохранить файл в нужную директорию или обработать его по-другому
    # Пример сохранения в папку 'uploads' в текущей директории
    file1.save('D:/monitor/instance/time_table/' + file1.filename)
    file2.save('D:/monitor/instance/time_table/' + file2.filename)

    return render_template('result.html', filename1=file1.filename, filename2=file2.filename)
if __name__ == '__main__':
    app.run(debug=True)
