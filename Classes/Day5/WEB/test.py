from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="htmlders"
)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/kayitol')
def kayitol():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cursor=db.cursor()
        cursor.execute("INSERT INTO kullanici_bilgisi (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        db.commit()
        db.close()
        return redirect(url_for('index.html'))
    
if __name__=='__main__':
    app.run(debug=True)