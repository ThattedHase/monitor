from flask import Flask, render_template, request, redirect, url_for
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_required




app = Flask(__name__)

UPLOAD_FOLDER = 'D:/monitor/instance/time_table'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

users = {'Ярослав': '1234','саня':'1234'}



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('main'))
        else:
            flash('Login unsuccessful')
            return render_template('login.html')

    return render_template('login.html')


@login_required
@app.route('/main')
def main():
    return render_template('main.html')


@login_required
@app.route('/upload')
def main1():
    return render_template('upload.html')

@login_required
@app.route('/uploadtest1')
def uploadtest1():
    return render_template('upl.html')

def create_folders():
    for folder_name in ['first', 'second']:
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def delete_existing_files():
    for folder_name in ['first', 'second']:
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
@login_required
@app.route('/uploadtest', methods=['POST'])
def upload_file():
    create_folders()

    delete_existing_files()

    if 'file1' not in request.files and 'file2' not in request.files:
        return render_template('result.html', filename1="файл не выбран", filename2="файл не выбран")

    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 and not file2:
        return render_template('result.html', filename1="файл не выбран", filename2="файл не выбран")

    file1_extension = secure_filename(file1.filename).split('.')[-1]
    file2_extension = secure_filename(file2.filename).split('.')[-1]

    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], 'first', f'first.{file1_extension}')
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], 'second', f'second.{file2_extension}')

    file1.save(file1_path)
    file2.save(file2_path)

    return render_template('result.html', filename1=file1.filename, filename2=file2.filename)

if __name__ == '__main__':
    app.run(debug=True)
