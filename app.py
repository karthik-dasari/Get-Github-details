from flask import Flask,render_template,redirect,url_for,request,session
from flask_mysqldb import MySQL

app=Flask(__name__)

app.secret_key='abcdefghijklmnopqrstuvwxyz'

app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='githubdetails'

mysql=MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/sendusername',methods=['POST','GET'])
def sendusername():
    gitHubUsername=request.form['gitHubUsername']
    cursor=mysql.connection.cursor()
    cursor.execute(' INSERT INTO data (username) VALUES(%s) ',(gitHubUsername,))
    mysql.connection.commit()
    cursor.close()
    return f"Done!!!"

@app.route('/getdata',methods=['POST','GET'])
def getdata():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM data')
    data=cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('history.html',data=data)

@app.route('/delete/<string:name_data>', methods = ['POST','GET'])
def delete(name_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data WHERE id = %s",(name_data,))
    mysql.connection.commit()
    return redirect('/getdata')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)