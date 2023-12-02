from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Простой "база данных" для хранения пользователей (в реальном проекте используйте базу данных)
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

if __name__ == '__main__':
    app.run(debug=True)
