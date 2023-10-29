from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Создание пользователя в базе данных
@app.route('/create_user', methods=['POST'])
def create_user(username,password):
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Пользователь с таким именем уже существует'})

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Пользователь успешно создан'})

create_user("SHKS","1234")


# Вход пользователя
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        # Здесь вы можете реализовать механизм входа для пользователя
        return jsonify({'message': 'Вход успешно выполнен'})
    return jsonify({'message': 'Неправильное имя пользователя или пароль'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
