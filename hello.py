from flask import Flask
from flask import request
from flask import render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'wf_tutorials'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def greeting():
    return "<h1 style='color:green'>Hello World!</h1>"


@app.route("/help")
def help():
    return "help me"


@app.route("/post/<id>")
def show_post(id):
    return "post id is " + id


@app.route("/bookmarks")
def display_bookmarks():
    bk = request.args.get("page", "1")
    return "the bookmark page is " + bk


@app.route("/index")
def index():
    users = ['user 1', 'user 2', 'users 3']
    data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials", 'users': users, 'isloggedin': True}
    return render_template('index.html', data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return request.form["username"] + " + " + request.form["password"]
    else:
        return render_template('login.html')


@app.route('/countries')
def show_countries():
    query = "SELECT * from countries LIMIT 50"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('countries.html', countries=data)


@app.route('/countries/create', methods=['POST', 'GET'])
def create_country():
    if request.method == "POST":
        newCountry = request.form["country"]
        query = "INSERT into countries(`country_name`) Values (%s)"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query, (newCountry,))
        conn.commit()
        return "Country created: " + newCountry
    else:
        return render_template('create_country.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')