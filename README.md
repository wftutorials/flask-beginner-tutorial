# Getting Started with Flask for python

In this tutorial we look at how we can development web applications
using the flask micro framework. Lets get started. You can visit the official website
[here](https://flask.palletsprojects.com/en/1.1.x/) for more information.

## Installation

To install `flask` we need to run a simple command. Of course we need to have
python installed on our computer first. Check out the link [here](https://www.python.org/downloads/) to 
learn how to download python.

```bash
pip install flask
```

Once you have `flask` installed we can get started.

## Hello World

Lets create a file called `hello.py`. 
Next we add the code below in it

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def greeting():
    return "<h1 style='color:green'>Hello World!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

You can see that first we imported `Flask`.
Then we create the `app` object.

Next we have our first route attached to the function `greeting()`.
This function returns some `html`.

Then we run using `app.run()`. This functions takes the `host` ip address. 
And that's it. Using flask is that simple. You can see the results below.

[hello_world.png]

We just created our first hello world app with flask.

# Working with routes

Lets create more routes with flask. Lets create a `help` route.

```python
@app.route("/help")
def help():
    return "help me"
```

Above we have a simple function called help. With an annotation pointing to
`/help`. The results is shown below.

[help_route.png]

## Placeholders in routes

We can add placeholders in our routes. Lets see how.

```python
@app.route("/post/<id>")
def show_post(id):
    return "post id is " + id
```

Above we create a function called `show_post`. The function
takes an argument id. In the annotation add a placeholder pattern `<id>`.
So we can have routes like `/post/5` or `post/3`. And we will have access to the `id`
inside the `show_post` function.

[route_placeholder.png]

## Getting url arguments

Lets see how we can get arguments from a url request.
First we need the `flask` request object.

```python
from flask import request
```

Then we can add the function below `display_bookmarks` to our `hello.py` file

```python
@app.route("/bookmarks")
def display_bookmarks():
    bk = request.args.get("page", "1")
    return "the bookmark page is " + bk
```

To get the argument from our url we can use the request object
and call `request.args.get()`. The results is shown below.

[url_arguments.png]

# Using templates

Lets see how we can use templates. Templates are `html` files.
When we learn how to do this we can create more complex layouts.

In order to use templates we must create a folder called `templates`. 
This is where flask looks for our `html` files.

After we do this we create a function called `index`.

```python
@app.route("/index")
def index():
    return render_template('index.html')
```

Above we call the `render_template` function. We pass in our `index.html` path.
In our `index.html` we add this content below

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Welcome to flask tutorial</h1>
<p style="font-size:20px;">This is a flask tutorial</p>
<ul>
    <li>My list item</li>
    <li>My list item</li>
</ul>
</body>
```

Lets see the results.

[rendering_html_templates.png]

## Passing data to our templates

We can pass data to our templates so we can use them inside our html files.
Lets see how. In our `index` function we created early we create an dictionary.

```python
data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials"}
```

Then we pass this in our `render_template` function as the second
argument.

```python
return render_template('index.html', data=data)
```

The full results is shown below

```python
@app.route("/index")
def index():
    data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials"}
    return render_template('index.html', data=data)
```

To use the variables within our templates we use `Jinja2` templates. You can learn more about them 
[here](https://jinja.palletsprojects.com/en/2.11.x/templates/).

Basically we use curly brackets `{{ }}` within our templates.

So the updated `index.html` is shown below.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ data.pagetitle }}</title>
</head>
<body>
<h1>{{ data.header }}</h1>
<p style="font-size:20px;">This is a flask tutorial</p>
<ul>
    <li>My list item</li>
    <li>My list item</li>
</ul>
</body>
</html>
```

Notice in our `title` element we have `data.pagetitle`.
In our `h1` element we have `data.header`. 

The results is shown below.

[passing_data_to_templates.png]

## Working with lists in templates

We can pass a list to our templates and render them. Lets see how.
First we create our list called `users`.

```python
users = ['user 1', 'user 2', 'users 3']
```

We add this to our dictionary

```python
data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials", 'users': users}
```

We pass this to our template.

```python
return render_template('index.html', data=data)
```

Now in our `index.html` we can loop our `items`.

```html
<ul>
    {% for item in data.users %}
        <li>{{  item }}</li>
    {% endfor %}
</ul>
```

You can see the full function here.

```python
@app.route("/index")
def index():
    users = ['user 1', 'user 2', 'users 3']
    data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials", 'users': users}
    return render_template('index.html', data=data)
```

Our full `index.html` can be found here -->

--comment --
# Rendering a list index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ data.pagetitle }}</title>
</head>
<body>
<h1>{{ data.header }}</h1>
<p style="font-size:20px;">This is a flask tutorial</p>
<ul>
    {% for item in data.users %}
        <li>{{  item }}</li>
    {% endfor %}
</ul>
</body>
</html>
```

-- end comment --

## Working with data in templates

We can access the entire dictionary in our template if we wanted to.
How? Lets see.

```html
<ul>
    {% for item in data.items() %}
        <li>{{  item }}</li>
    {% endfor %}
</ul>
```

We use the `dict.items()` function to loop our data. The results is shown below

[looping_dictionary.png]

So we can use normal python functions within our templates. Try it out.

## Conditionally rendering elements

Lets add some `if` statements in our template.

We add a loggedin variable in our dictionary.

```python
data = {'isloggedin': True}
```

Now in our template we change conditionally render `html` based on this.

```html
{% if data.isloggedin %}
    <p>User is logged in</p>
{% endif %}
```

Once `isloggedin` is `True` we will see the `p` element.

[conditionally_render_html.png]

## Else statement

Or we can add a else statement if our condition fails.

```html
{% if data.isloggedin %}
    <p>User is logged in</p>
{% else %}
   <p>User is NOT logged in</p>
{% endif %}
```

# Working with forms

Lets create a form and submit data. Let see how we can do this with flask.
We will create a login form. Create a `login.html` in the templates directory and add the
content below.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login Page</title>
</head>
<body>
<h3>Login Form</h3>
<form method="post">
    <Label>Username: </Label><input type="text" name="username"/><br>
    <label>Password: </label><input type="password" name="password"/><br>
    <input type="submit"/>
</form>
</body>
</html>
```

Our code is very simple. We create a `login` function to match our template.

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
```

Of note is the second argument in `app.route`. This says that this route can accept both
`POST` and `GET` requests.

The results is shown below.

[login_form.png]

## Getting POST data from a form

To get post data from a submitted form we can call `request.form[]`.
Referencing the parameter from the form we want. We show this below.

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return request.form["username"] + " + " + request.form["password"]
    else:
        return render_template('login.html')
```

Add the above code. Update your `login` route function to look like above.
First thing we do is to check if the `request.method` is either post or get.
If it is a POST we use the form data dictionary via `request.form` to get our
parameters from the form as shown below

```python
return request.form["username"] + " + " + request.form["password"]
```

We return the submitted data. Let see how this looks in practice.

[submit_form.gif]

Remember that `request.form` is a dictionary so we can use dictionary methods like

```python
for value in request.form.items() # loop form data

request.form.get("") # get a value from the dictionary
```

You get the point.

# Working with databases

To get started using `MySQL` we first have to install a package.

```bash
pip install flask-mysql
```

Above we install `flask-mysql` you can learn more about it [here](https://flask-mysql.readthedocs.io/en/latest/).
Now lets go through the steps.

First we import it 

```python
from flaskext.mysql import MySQL
```

Then we create the object above the app object

```python
mysql = MySQL()
app = Flask(__name__)
```

Now add your configurations. This is the database connection information.

```python
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'wf_tutorials'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
```

Now we initialize mysql via the app.

```python
mysql.init_app(app)
```

Next we create a `countries.html` view.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of Users</title>
</head>
<body>
<h1>List of Countries</h1>
<ul>
    {% for country in countries %}
    <li>{{ country[1] }} | of id {{ country[0] }}</li>
    {% endfor %}
</ul>
</body>
</html>
```

We are accepting data to be passed called `countries`. We will loop these values and generate a list.
Every item in the tuple will be another tuple so we get those values via index `country[1]`.

Now in the code we create a function to show our countries.

First we create our route

```python
@app.route('/countries')
def show_countries():
    return render_template('countries.html')
```

Next we add our mysql connections.

```python
@app.route('/countries')
def show_countries():
    query = "SELECT * from countries LIMIT 50"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('countries.html')
```

Finally we pass our data to the `countries.html`

```python
@app.route('/countries')
def show_countries():
    query = "SELECT * from countries LIMIT 50"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('countries.html', countries=data)
```

This should give us the results shown below.

[showing_countries_from_db.png]

## Save to Db with forms

Lets create a form so we can save a new country. First we create a html file called
`create_country.html`.


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Country</title>
</head>
<body>
<h3>Create Country</h3>
<form method="post">
    <Label>Add Country: </Label><input type="text" name="country"/><br>
    <input type="submit"/>
</form>
</body>
</html>
```

This results in the layout below.

[create_country_layout.png]

Next we create our route and function.

```python
@app.route('/countries/create')
def create_country():
    return render_template('create_country.html')
```

Notice our route uses `/countries/create`. You can do this.

[create_country_route.png]

Next we want to check for `POST` requests.

```python
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
```

Above we check for the post request. Then we create our connection object
and get a cursor. 

After we call the `cursor.execute()` and pass in our `query` this will allow use to insert data into our database.
If the request is not post we show our `create_country.html` form.

Lets see the results below.

[adding_a_country.gif]

This will add the country to our database.

[added_country_indb.png]

# Working with assets

Lets add a css file to our app. First we create a folder called `static`.
Then within the static folder we create a `main.css` file and we add some styles.
Check them out here -->

-- Comment --

# Style for our main.css

I got these styles via [sanwebe](https://www.sanwebe.com/2014/08/css-html-forms-designs). Great form styles.

```css

.form-style-1 {
	margin:10px auto;
	max-width: 400px;
	padding: 20px 12px 10px 20px;
	font: 13px "Lucida Sans Unicode", "Lucida Grande", sans-serif;
}
.form-style-1 li {
	padding: 0;
	display: block;
	list-style: none;
	margin: 10px 0 0 0;
}
.form-style-1 label{
	margin:0 0 3px 0;
	padding:0px;
	display:block;
	font-weight: bold;
}
.form-style-1 input[type=text],
.form-style-1 input[type=date],
.form-style-1 input[type=datetime],
.form-style-1 input[type=number],
.form-style-1 input[type=search],
.form-style-1 input[type=time],
.form-style-1 input[type=url],
.form-style-1 input[type=email],
textarea,
select{
	box-sizing: border-box;
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	border:1px solid #BEBEBE;
	padding: 7px;
	margin:0px;
	-webkit-transition: all 0.30s ease-in-out;
	-moz-transition: all 0.30s ease-in-out;
	-ms-transition: all 0.30s ease-in-out;
	-o-transition: all 0.30s ease-in-out;
	outline: none;
}
.form-style-1 input[type=text]:focus,
.form-style-1 input[type=date]:focus,
.form-style-1 input[type=datetime]:focus,
.form-style-1 input[type=number]:focus,
.form-style-1 input[type=search]:focus,
.form-style-1 input[type=time]:focus,
.form-style-1 input[type=url]:focus,
.form-style-1 input[type=email]:focus,
.form-style-1 textarea:focus,
.form-style-1 select:focus{
	-moz-box-shadow: 0 0 8px #88D5E9;
	-webkit-box-shadow: 0 0 8px #88D5E9;
	box-shadow: 0 0 8px #88D5E9;
	border: 1px solid #88D5E9;
}
.form-style-1 .field-divided{
	width: 49%;
}

.form-style-1 .field-long{
	width: 100%;
}
.form-style-1 .field-select{
	width: 100%;
}
.form-style-1 .field-textarea{
	height: 100px;
}
.form-style-1 input[type=submit], .form-style-1 input[type=button]{
	background: #4B99AD;
	padding: 8px 15px 8px 15px;
	border: none;
	color: #fff;
}
.form-style-1 input[type=submit]:hover, .form-style-1 input[type=button]:hover{
	background: #4691A4;
	box-shadow:none;
	-moz-box-shadow:none;
	-webkit-box-shadow:none;
}
.form-style-1 .required{
	color:red;
}

```

Now in our `create_country.html` we create our style link

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css') }}"/>
```

Notice our `url_for` function in double curly brackets. This creates the url path for our file.
Now when we run the server we can see our results with our nicely styles form.

[styling_a_form.png]

## Adding Javascript assets

You can do the same thing above for javascript files. Lets just try it.
We create a file called `main.js` and add the content below

```javascript
document.getElementById('button').onclick = function changeContent() {

    alert("clicked me")

}
```

Now in our `countries.html` file we can add our `script`.

```html
<script src="{{ url_for('static', filename='main.js') }}"></script>
```

Of course we need to add our button somewhere.

```html
<button id="button">Click me</button>
```

That is it. Lets see the results.

[javascript_asset.gif]

# Creating an API

Lets create an api. First we create a function called `api`.
Then we add the code below. 

```python
@app.route('/api/users', methods=['GET','POST'])
def api():
    if request.method == "GET":
        query = "SELECT * from countries LIMIT 50"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data=data)
    if request.method == "POST":
        newCountry = request.form["country"]
        query = "INSERT into countries(`country_name`) Values (%s)"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query, (newCountry,))
        conn.commit()
        return jsonify(results="Country created: " + newCountry)
```

Above we have one route - `/api/users`. Next we check for different
type of requests. So for `GET` we return a list of countries.

For `POST` we attempt to add a new country. We can test this with
`POSTMAN`. Check out the results below

Our `GET` request

[api_get_request.png]

Our `POST` request

[add_country_via_api.png]

Notice we are using `jsonify` to convert our cursor to json data. We can access jsonify from
`flask`.

```python
from flask import jsonify
```

# User Authentication

How can we login and logout users so we can secure your web application. Let see how.
We are going to use the package `flask-login` you can learn more about it [here](https://flask-login.readthedocs.io/en/latest/#installation)

First we need to install it via pip.

```bash
pip install flask-login
```

Next we need some imports

```python
from flask_login import current_user, login_user, LoginManager, logout_user, login_required
```

Now we create a `loginManger` object and add it to our app object

```python
login_manager = LoginManager()
login_manager.init_app(app)
```

We add our secret key because we are using sessions and flask requires this

```python
app = Flask(__name__)
app.secret_key = "sasasdf2fb3443b4"
```

Now we create a user class with the required methods in it.
View our user class here -->

```python
class User:
    name = ""
    password = ""
    id = 0

    def __init__(self, name="", password=""):
        self.name = name
        self.password = password

    def is_authenticated(self):
        query = "SELECT * from yii_users WHERE username=%s AND password=%s LIMIT 1"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query, (self.name, self.password))
        data = cursor.fetchone()
        if data is None:
            return False
        else:
            self.id = data[0]
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if self.id == 0:
            return True
        else:
            return False

    def get_id(self):
        return str(self.id).encode("utf-8").decode("utf-8")

    @staticmethod
    def get(user_id):
        query = "SELECT * from yii_users WHERE id =%s LIMIT 1"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        data = cursor.fetchone()
        user = User()
        user.id = user_id
        user.name = data[1]
        user.password = data[2]
        return user
```

Finally we add a function to load our user model once the user is logged in.

```python
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
```

Now in our login function we can add the following code

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        user = User(name, password)
        if user.is_authenticated():
            login_user(user)
            return "logged in good"
        else:
            return "log in not good"
    else:
        return render_template('login.html')

```

That is it. We can now log in as a user. In our `login.html` we add some code
to tell the difference.

```html
<h3>Login Form</h3>
{% if current_user.is_authenticated %}
<p>user is logged in</p>
<p>Hi {{ current_user.name }}!</p>
{% else %}
<form method="post">
    <Label>Username: </Label><input type="text" name="username"/><br>
    <label>Password: </label><input type="password" name="password"/><br>
    <input type="submit"/>
</form>
{% endif %}
```

We also add a logout route.

```python
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')
```

We use the `redirect` function to send the user to a different route after
logging out.

The results can can be seen below.

[log_in_log_out_example.gif]

# Conclusion

You have just completed a crash course in flask. You can now get started building web applications.
There is alot more to learn. Thanks for taking the time to learn with wfTutorials.
