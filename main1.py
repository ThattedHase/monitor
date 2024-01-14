from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upl.html')

@app.route('/upload', methods=['POST'])
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
