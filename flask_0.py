from flask import Flask, render_template, url_for

menu = ["1", "2", "3", "4"]

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title = 'Про Flask', menu = menu)
@app.route('/about')
def about():
    return render_template('about.html', title = 'О сайте')
@app.route('/help')
def help():
    return render_template('help.html', title = 'Помощь')
@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакты')

if __name__ =="__main__":
    app.run(debug = True)