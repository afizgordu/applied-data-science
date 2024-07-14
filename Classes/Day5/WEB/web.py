from flask import   Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
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

@app.route('/kayitol', methods=['POST'])
def kayitol():
    if request.method == 'POST':
        name= request.form['name']
        email= request.form ['email']
        password= request.form['password']

        cursor=mydb.cursor()
        cursor.execute('insert into users (name, email, password) values(%s, %s, %s)', (name, email, password))
        mydb.commit()
        mydb.close()
        return redirect(url_for('index'))

#cursor=mydb.cursor()
#name="Ahmet Faruk İzgördü"
#email="ahmetfaruk@izgordu.com"
#password="test"
#user_id=1

#cursor.execute("UPDATE users SET name=%s, email=%s, password=%s where id=%s", (name,email,password,user_id))
#mydb.commit()
#mydb.close()

cursor=mydb.cursor()
user_id=1
cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
mydb.commit()
mydb.close()


if __name__ == '__main__':
    app.run(debug=True)
    

    