from flask import Flask, render_template, Request,request, flash, redirect, url_for, send_from_directory, jsonify, session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from datetime import timedelta
import os
from werkzeug.utils import secure_filename
import pandas as pd





app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = '93422'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['UPLOAD_FOLDER1'] = 'D:/monitor/instance/time_table/monday'
app.config['UPLOAD_FOLDER2'] = 'D:/monitor/instance/time_table/tuesday'
app.config['UPLOAD_FOLDER3'] = 'D:/monitor/instance/time_table/wednesday'
app.config['UPLOAD_FOLDER4'] = 'D:/monitor/instance/time_table/thursday'
app.config['UPLOAD_FOLDER5'] = 'D:/monitor/instance/time_table/friday'
app.config['UPLOAD_FOLDER6'] = 'D:/monitor/instance/time_table/saturday'
app.config['UPLOAD_FOLDER7'] = 'D:/monitor/instance/time_table/sunday'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main'))
        else:
            flash('Login failed. Check your username and password.', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return redirect(url_for('register'))
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        
        return redirect(url_for('main'))
    
    return render_template('register.html')


@login_required
@app.route('/main')
def main():
    return render_template('main.html')

@login_required
@app.route('/monday')
def monday():
    a1 = '/upload_monday1'
    a2 = '/upload_monday2'
    return render_template('monday.html',a1=a1,a2=a2)

@login_required
@app.route('/tuesday')
def tuesday():
    a1 = '/upload_tuesday1'
    a2 = '/upload_tuesday2'

    return render_template('tuesday.html',a1=a1,a2=a2)

@login_required
@app.route('/wednesday')
def wednesday():
    a1 = '/upload_wednesday1'
    a2 = '/upload_wednesday2'
    return render_template('wednesday.html',a1=a1,a2=a2)


@login_required
@app.route('/thursday')
def thursday():
    a1 = '/upload_thursday1'
    a2 = '/upload_thursday2'

    return render_template('thursday.html',a1=a1,a2=a2)

@login_required
@app.route('/friday')
def friday():
    a1 = '/upload_friday1'
    a2 = '/upload_friday2'
    return render_template('friday.html',a1=a1,a2=a2)

@login_required
@app.route('/saturday')
def saturday():
    a1 = '/upload_saturday1'
    a2 = '/upload_saturday2'

    return render_template('saturday.html',a1=a1,a2=a2)

@login_required
@app.route('/sunday')
def sunday():
    a1 = '/upload_sunday1'
    a2 = '/upload_sunday2'

    return render_template('sunday.html',a1=a1,a2=a2)




@login_required
@app.route('/upload')
def main1():
    return render_template('upload.html')

@login_required
@app.route('/uploadtest1')
def uploadtest1():
    return render_template('upl.html')

def create_folders1(a):
    for folder_name in ['first']:
        folder_path = os.path.join(app.config[a], folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def create_folders2(a):
    for folder_name in ['second']:
        folder_path = os.path.join(app.config[a], folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def delete_existing_files1(a):
    for folder_name in ['first']:
        folder_path = os.path.join(app.config[a], folder_name)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)


def delete_existing_files2(a):
    for folder_name in ['second']:
        folder_path = os.path.join(app.config[a], folder_name)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            
@login_required
@app.route('/upload_monday1', methods=['POST'])
#monday1
def upload_file1_monday():
    a = 'UPLOAD_FOLDER1'
    create_folders1(a)
    delete_existing_files1(a)

    print()
    file1 = request.files.get('file1')
    file1_extension = secure_filename(file1.filename).split('.')[-1]
    
    if not file1:
        filename1 = "файл не выбран"
    else:
        filename1 = file1.filename
        file1_path = os.path.join(app.config[a], 'first', f'first.{file1_extension}')
        file1.save(file1_path)
    return render_template('result.html', filename=filename1)
#monday2
@login_required
@app.route('/upload_monday2', methods=['POST'])
def upload_file2_monday(a):
    create_folders2(a)
    delete_existing_files2(a)


    file2 = request.files.get('file2')
    file2_extension = secure_filename(file2.filename).split('.')[-1]
    print(file2)
    
    if not file2:
        filename2 = "файл не выбран"
    else:
        filename2 = file2.filename
        file2_path = os.path.join(app.config[a], 'second', f'second.{file2_extension}')
        file2.save(file2_path)
        
    return render_template('result.html', filename=filename2)

#tuesday1
@login_required
@app.route('/upload_tuesday1', methods=['POST'])
def upload_file1_tuesday():
    a = 'UPLOAD_FOLDER2'
    create_folders1(a)
    delete_existing_files1(a)

    print()
    file1 = request.files.get('file1')
    file1_extension = secure_filename(file1.filename).split('.')[-1]
    
    if not file1:
        filename1 = "файл не выбран"
    else:
        filename1 = file1.filename
        file1_path = os.path.join(app.config[a], 'first', f'first.{file1_extension}')
        file1.save(file1_path)
    return render_template('result.html', filename=filename1)

#tuesday2
@login_required
@app.route('/upload_tuesday2', methods=['POST'])
def upload_file2_tuesday():
    a = 'UPLOAD_FOLDER2'
    create_folders2(a)
    delete_existing_files2(a)


    file2 = request.files.get('file2')
    file2_extension = secure_filename(file2.filename).split('.')[-1]
    print(file2)
    
    if not file2:
        filename2 = "файл не выбран"
    else:
        filename2 = file2.filename
        file2_path = os.path.join(app.config[a], 'second', f'second.{file2_extension}')
        file2.save(file2_path)
        
    return render_template('result.html', filename=filename2)


#wednesday1
@login_required
@app.route('/upload_wednesday1', methods=['POST'])
def upload_file1_wednesday():
    a = 'UPLOAD_FOLDER3'
    create_folders1(a)
    delete_existing_files1(a)

    print()
    file1 = request.files.get('file1')
    file1_extension = secure_filename(file1.filename).split('.')[-1]
    
    if not file1:
        filename1 = "файл не выбран"
    else:
        filename1 = file1.filename
        file1_path = os.path.join(app.config[a], 'first', f'first.{file1_extension}')
        file1.save(file1_path)
    return render_template('result.html', filename=filename1)
#wednesday2
@login_required
@app.route('/upload_wednesday2', methods=['POST'])
def upload_file2_wednesday():
    a = 'UPLOAD_FOLDER3'
    create_folders2(a)
    delete_existing_files2(a)


    file2 = request.files.get('file2')
    file2_extension = secure_filename(file2.filename).split('.')[-1]
    print(file2)
    
    if not file2:
        filename2 = "файл не выбран"
    else:
        filename2 = file2.filename
        file2_path = os.path.join(app.config[a], 'second', f'second.{file2_extension}')
        file2.save(file2_path)
        
    return render_template('result.html', filename=filename2)

#thursday1
@login_required
@app.route('/upload_thursday1', methods=['POST'])
def upload_file1_thursday():
    a = 'UPLOAD_FOLDER4'
    create_folders1(a)
    delete_existing_files1(a)

    print()
    file1 = request.files.get('file1')
    file1_extension = secure_filename(file1.filename).split('.')[-1]
    
    if not file1:
        filename1 = "файл не выбран"
    else:
        filename1 = file1.filename
        file1_path = os.path.join(app.config[a], 'first', f'first.{file1_extension}')
        file1.save(file1_path)
    return render_template('result.html', filename=filename1)

#thursday2
@login_required
@app.route('/upload_thursday2', methods=['POST'])
def upload_file2_thursday():
    a = 'UPLOAD_FOLDER4'
    create_folders2(a)
    delete_existing_files2(a)


    file2 = request.files.get('file2')
    file2_extension = secure_filename(file2.filename).split('.')[-1]
    print(file2)
    
    if not file2:
        filename2 = "файл не выбран"
    else:
        filename2 = file2.filename
        file2_path = os.path.join(app.config[a], 'second', f'second.{file2_extension}')
        file2.save(file2_path)
        
    return render_template('result.html', filename=filename2)

#friday1
@login_required
@app.route('/upload_friday1', methods=['POST'])
def upload_file1_friday():
    a = 'UPLOAD_FOLDER5'
    create_folders1(a)
    delete_existing_files1(a)

    print()
    file1 = request.files.get('file1')
    file1_extension = secure_filename(file1.filename).split('.')[-1]
    
    if not file1:
        filename1 = "файл не выбран"
    else:
        filename1 = file1.filename
        file1_path = os.path.join(app.config[a], 'first', f'first.{file1_extension}')
        file1.save(file1_path)
    return render_template('result.html', filename=filename1)

#friday2
@login_required
@app.route('/upload_friday2', methods=['POST'])
def upload_file2_friday():
    a = 'UPLOAD_FOLDER5'
    create_folders2(a)
    delete_existing_files2(a)


    file2 = request.files.get('file2')
    file2_extension = secure_filename(file2.filename).split('.')[-1]
    print(file2)
    
    if not file2:
        filename2 = "файл не выбран"
    else:
        filename2 = file2.filename
        file2_path = os.path.join(app.config[a], 'second', f'second.{file2_extension}')
        file2.save(file2_path)
        
    return render_template('result.html', filename=filename2)


#saturday1
@login_required
@app.route('/upload_saturday1', methods=['POST'])
def upload_file1_saturday():
    a = 'UPLOAD_FOLDER6'
    create_folders1(a)
    delete_existing_files1(a)

    print()
    file1 = request.files.get('file1')
    file1_extension = secure_filename(file1.filename).split('.')[-1]
    
    if not file1:
        filename1 = "файл не выбран"
    else:
        filename1 = file1.filename
        file1_path = os.path.join(app.config[a], 'first', f'first.{file1_extension}')
        file1.save(file1_path)
    return render_template('result.html', filename=filename1)
#saturday2
@login_required
@app.route('/upload_saturday2', methods=['POST'])
def upload_file2_saturday():
    a = 'UPLOAD_FOLDER6'
    create_folders2(a)
    delete_existing_files2(a)


    file2 = request.files.get('file2')
    file2_extension = secure_filename(file2.filename).split('.')[-1]
    print(file2)
    
    if not file2:
        filename2 = "файл не выбран"
    else:
        filename2 = file2.filename
        file2_path = os.path.join(app.config[a], 'second', f'second.{file2_extension}')
        file2.save(file2_path)
        
    return render_template('result.html', filename=filename2)

#sunday1
@login_required
@app.route('/upload_sunday1', methods=['POST'])
def upload_file1_sunday():
    a = 'UPLOAD_FOLDER7'
    create_folders1(a)
    delete_existing_files1(a)

    print()
    file1 = request.files.get('file1')
    file1_extension = secure_filename(file1.filename).split('.')[-1]
    
    if not file1:
        filename1 = "файл не выбран"
    else:
        filename1 = file1.filename
        file1_path = os.path.join(app.config[a], 'first', f'first.{file1_extension}')
        file1.save(file1_path)
    return render_template('result.html', filename=filename1)

#sunday2
@login_required
@app.route('/upload_sunday2', methods=['POST'])
def upload_file2_sunday():
    a = 'UPLOAD_FOLDER7'
    create_folders2(a)
    delete_existing_files2(a)


    file2 = request.files.get('file2')
    file2_extension = secure_filename(file2.filename).split('.')[-1]
    print(file2)
    
    if not file2:
        filename2 = "файл не выбран"
    else:
        filename2 = file2.filename
        file2_path = os.path.join(app.config[a], 'second', f'second.{file2_extension}')
        file2.save(file2_path)
        
    return render_template('result.html', filename=filename2)





    


if __name__ == '__main__':
    app.run(debug=True)

    

